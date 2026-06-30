import streamlit as st
import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from style import inject_global_css, sidebar_brand, eyebrow, sign_row, GOLD, NAVY_DARK, CREAM, CREAM_DIM

# ── Konfigurasi ──
IMG_SIZE = 640
CLASSES = [
    '__background__',
    'larangan_memutar_balik',
    'penyeberangan_pejalan_kaki',
    'larangan_berhenti',
    'simpang_tiga',
    'simpang_empat'
]
NAMA_TAMPIL = {
    'larangan_memutar_balik': 'Larangan Memutar Balik',
    'penyeberangan_pejalan_kaki': 'Penyeberangan Pejalan Kaki',
    'larangan_berhenti': 'Larangan Berhenti',
    'simpang_tiga': 'Simpang Tiga',
    'simpang_empat': 'Simpang Empat',
}
MODEL_PATH = 'model_rambu_full.pth'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

val_transform = A.Compose([
    A.Resize(IMG_SIZE, IMG_SIZE),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2()
], bbox_params=A.BboxParams(format='pascal_voc', label_fields=['class_labels'], min_visibility=0.3))


@st.cache_resource
def load_model():
    model = torch.load(MODEL_PATH, map_location=device, weights_only=False)
    model.to(device)
    model.eval()
    return model


def deteksi(model, img_asli, conf_thresh):
    transformed = val_transform(image=img_asli, bboxes=[], class_labels=[])
    img_tensor = transformed['image'].unsqueeze(0).to(device)

    with torch.no_grad():
        pred = model(img_tensor)[0]

    keep = pred['scores'] >= conf_thresh
    boxes = pred['boxes'][keep].cpu()
    labels = pred['labels'][keep].cpu()
    scores = pred['scores'][keep].cpu()

    img_tampil = transformed['image'].permute(1, 2, 0).numpy()
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    img_tampil = np.clip(img_tampil * std + mean, 0, 1)

    return img_tampil, boxes, labels, scores


def gambar_hasil(img_tampil, boxes, labels, scores, classes):
    fig, ax = plt.subplots(1, figsize=(7, 7))
    fig.patch.set_facecolor(NAVY_DARK)
    ax.imshow(img_tampil)

    for box, label, score in zip(boxes, labels, scores):
        x1, y1, x2, y2 = box.tolist()
        rect = patches.Rectangle((x1, y1), x2 - x1, y2 - y1,
                                  linewidth=2.5, edgecolor=GOLD, facecolor='none')
        ax.add_patch(rect)
        nama_kelas = classes[label.item()]
        label_tampil = NAMA_TAMPIL.get(nama_kelas, nama_kelas)
        ax.text(x1, max(y1 - 8, 10), f'{label_tampil}  {score:.0%}',
                color=NAVY_DARK, fontsize=9, fontweight='bold',
                bbox=dict(facecolor=GOLD, alpha=0.95, pad=3, edgecolor='none'))
    ax.axis('off')
    plt.tight_layout()
    return fig


# ── Page setup ──
st.set_page_config(page_title="RambuVision — Deteksi", page_icon="🔺", layout="wide")
inject_global_css()

with st.sidebar:
    sidebar_brand()
    st.page_link("app.py", label="Deteksi Rambu")
    st.page_link("pages/1_Ensiklopedia_Rambu.py", label="Ensiklopedia Rambu")
    st.page_link("pages/2_Statistik_Model.py", label="Statistik Model")
    st.page_link("pages/3_Galeri_Deteksi.py", label="Galeri Deteksi")
    st.page_link("pages/4_Tentang_Proyek.py", label="Tentang Proyek")
    st.markdown('<hr class="thin-divider">', unsafe_allow_html=True)
    st.markdown("##### Pengaturan Deteksi")
    conf_thresh = st.slider("Ambang kepercayaan", min_value=0.10, max_value=0.99, value=0.70, step=0.05,
                             help="Naikkan jika model terlalu sering salah deteksi. Turunkan jika rambu asli tidak terdeteksi.")

eyebrow("Deteksi Real-Time")
st.title("Kenali Rambu dalam Sekali Unggah")
st.write(
    "Unggah foto rambu lalu lintas, dan model Faster R-CNN akan menandai lokasinya "
    "serta menyebutkan jenisnya beserta tingkat kepercayaan."
)

col_upload, col_result = st.columns([1, 1.3], gap="large")

with col_upload:
    st.markdown('<div class="rambu-card">', unsafe_allow_html=True)
    st.markdown("**Unggah Gambar**")
    uploaded_file = st.file_uploader("Pilih gambar rambu (.jpg, .jpeg, .png)", type=['jpg', 'jpeg', 'png'],
                                      label_visibility="collapsed")
    st.caption("Pastikan rambu terlihat jelas dan tidak terlalu jauh dari kamera untuk hasil terbaik.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="rambu-card">', unsafe_allow_html=True)
    st.markdown("**Kelas yang Dikenali**")
    for i, c in enumerate(CLASSES[1:], start=1):
        sign_row(f"{i:02d}", NAMA_TAMPIL.get(c, c))
    st.markdown('</div>', unsafe_allow_html=True)

with col_result:
    if uploaded_file is not None:
        model = load_model()
        img_pil = Image.open(uploaded_file).convert('RGB')
        img_asli = np.array(img_pil)

        with st.spinner('Memindai gambar...'):
            img_tampil, boxes, labels, scores = deteksi(model, img_asli, conf_thresh)

        if len(boxes) == 0:
            st.markdown(
                f"""<div class="rambu-card-gold">
                <span class="badge-warning">Tidak terdeteksi</span>
                <p style="margin-top:0.7rem;">Tidak ada rambu yang dikenali pada gambar ini.
                Coba turunkan ambang kepercayaan di sidebar, atau pastikan gambar termasuk
                salah satu dari 5 jenis rambu yang dilatih.</p>
                </div>""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<span class="badge-success">{len(boxes)} rambu terdeteksi</span>',
                unsafe_allow_html=True,
            )
            fig = gambar_hasil(img_tampil, boxes, labels, scores, CLASSES)
            st.pyplot(fig)

            st.markdown("**Rincian Deteksi**")
            for box, label, score in zip(boxes, labels, scores):
                nama_kelas = CLASSES[label.item()]
                label_tampil = NAMA_TAMPIL.get(nama_kelas, nama_kelas)
                sign_row("&bull;", label_tampil, f"{score:.1%}")
    else:
        st.markdown(
            f"""<div class="rambu-card" style="text-align:center; padding:3.5rem 1.5rem;">
            <div style="font-family:'Fraunces',serif; font-size:1.1rem; color:{CREAM}; opacity:0.6;">
            Hasil deteksi akan tampil di sini setelah gambar diunggah.</div>
            </div>""",
            unsafe_allow_html=True,
        )
