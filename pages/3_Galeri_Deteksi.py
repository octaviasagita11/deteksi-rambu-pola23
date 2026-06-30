import streamlit as st
import os
from style import inject_global_css, sidebar_brand, eyebrow, CREAM_DIM

st.set_page_config(page_title="RambuVision — Galeri", page_icon="🖼️", layout="wide")
inject_global_css()

with st.sidebar:
    sidebar_brand()
    st.page_link("app.py", label="Deteksi Rambu")
    st.page_link("pages/1_Ensiklopedia_Rambu.py", label="Ensiklopedia Rambu")
    st.page_link("pages/2_Statistik_Model.py", label="Statistik Model")
    st.page_link("pages/3_Galeri_Deteksi.py", label="Galeri Deteksi")
    st.page_link("pages/4_Tentang_Proyek.py", label="Tentang Proyek")

eyebrow("Contoh Hasil")
st.title("Galeri Deteksi")
st.write(
    "Kumpulan contoh hasil deteksi pada data uji. Tambahkan gambar Anda sendiri ke folder "
    "`assets/galeri/` agar tampil di halaman ini."
)

GALERI_DIR = "assets/galeri"

if os.path.isdir(GALERI_DIR) and len(os.listdir(GALERI_DIR)) > 0:
    files_img = [f for f in os.listdir(GALERI_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    cols = st.columns(3)
    for i, fname in enumerate(files_img):
        with cols[i % 3]:
            st.markdown('<div class="rambu-card" style="padding:0.6rem;">', unsafe_allow_html=True)
            st.image(os.path.join(GALERI_DIR, fname), use_container_width=True)
            st.caption(fname)
            st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown(
        f"""
        <div class="rambu-card" style="text-align:center; padding:3.5rem 1.5rem;">
            <p style="color:{CREAM_DIM};">
            Belum ada gambar di galeri. Tambahkan file <code>.jpg</code>/<code>.png</code>
            ke folder <code>assets/galeri/</code>, lalu muat ulang halaman ini.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<hr class="thin-divider">', unsafe_allow_html=True)
st.info(
    "Tip: simpan hasil deteksi terbaik dari halaman **Deteksi Rambu** "
    "(klik kanan pada gambar hasil → Simpan gambar) lalu pindahkan ke folder galeri ini."
)
