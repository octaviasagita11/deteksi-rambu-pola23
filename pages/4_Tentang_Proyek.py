import streamlit as st
from style import inject_global_css, sidebar_brand, eyebrow, stat_tile, GOLD, CREAM_DIM

st.set_page_config(page_title="RambuVision — Tentang", page_icon="ℹ️", layout="wide")
inject_global_css()

with st.sidebar:
    sidebar_brand()
    st.page_link("app.py", label="Deteksi Rambu")
    st.page_link("pages/1_Ensiklopedia_Rambu.py", label="Ensiklopedia Rambu")
    st.page_link("pages/2_Statistik_Model.py", label="Statistik Model")
    st.page_link("pages/3_Galeri_Deteksi.py", label="Galeri Deteksi")
    st.page_link("pages/4_Tentang_Proyek.py", label="Tentang Proyek")

eyebrow("Di Balik Sistem")
st.title("Tentang Proyek")
st.write(
    "RambuVision adalah sistem deteksi rambu lalu lintas Indonesia berbasis deep learning, "
    "dikembangkan sebagai proyek riset akademik."
)

c1, c2, c3, c4 = st.columns(4)
with c1:
    stat_tile("Arsitektur", "Faster R-CNN", "ResNet-50 + FPN")
with c2:
    stat_tile("Kelas Dilatih", "5", "jenis rambu Indonesia")
with c3:
    stat_tile("Epoch Training", "30", "konvergen di epoch 17")
with c4:
    stat_tile("Framework", "PyTorch", "+ Albumentations")

st.markdown('<hr class="thin-divider">', unsafe_allow_html=True)

col_kiri, col_kanan = st.columns(2, gap="large")

with col_kiri:
    st.subheader("Cara Kerja Sistem")
    langkah = [
        ("1", "Pra-pemrosesan", "Gambar diresize ke 640×640 piksel dan dinormalisasi sesuai statistik ImageNet."),
        ("2", "Ekstraksi Fitur", "ResNet-50 + FPN mengekstrak fitur visual multi-skala dari gambar."),
        ("3", "Usulan Wilayah", "Region Proposal Network (RPN) mengusulkan area yang mungkin berisi rambu."),
        ("4", "Klasifikasi & Lokalisasi", "Setiap usulan area diklasifikasikan jenis rambunya dan koordinat kotaknya disempurnakan."),
        ("5", "Penyaringan", "Hanya deteksi dengan confidence di atas ambang batas yang ditampilkan."),
    ]
    for no, judul, desk in langkah:
        st.markdown(
            f"""
            <div style="display:flex; gap:1rem; margin-bottom:1rem;">
                <div style="font-family:'JetBrains Mono',monospace; font-weight:700; color:{GOLD};
                            font-size:1.1rem; min-width:1.6rem;">{no}</div>
                <div>
                    <div style="font-weight:600;">{judul}</div>
                    <div style="color:{CREAM_DIM}; font-size:0.92rem;">{desk}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col_kanan:
    st.subheader("Metodologi Pelatihan")
    st.markdown(
        f"""
        <div class="rambu-card">
        <ul style="margin:0; padding-left:1.1rem; line-height:1.9;">
            <li><strong>Pembagian data:</strong> 70% latih, 20% validasi, 10% uji — dengan stratifikasi per kelas.</li>
            <li><strong>Augmentasi:</strong> flip horizontal, rotasi ±15°, variasi kecerahan/kontras, blur, dan variasi warna — hanya pada data latih.</li>
            <li><strong>Optimizer:</strong> SGD dengan momentum 0.9 dan weight decay 0.0005.</li>
            <li><strong>Penjadwal Learning Rate:</strong> StepLR, menurun 10× setiap 10 epoch.</li>
            <li><strong>Model terbaik:</strong> dipilih otomatis berdasarkan validation loss terendah selama pelatihan.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Keterbatasan")
    st.markdown(
        f"""
        <div class="rambu-card-gold">
        <p style="margin:0;">Model ini bersifat <em>closed-set</em> — hanya mengenali 5 kelas yang dilatih.
        Pada gambar dengan latar kompleks (multi-objek, watermark, kondisi pencahayaan ekstrem),
        presisi lokasi kotak dan ketahanan terhadap salah deteksi masih dapat ditingkatkan lebih lanjut.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
