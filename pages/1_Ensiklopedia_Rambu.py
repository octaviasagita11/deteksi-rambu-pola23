import streamlit as st
from style import inject_global_css, sidebar_brand, eyebrow, GOLD

st.set_page_config(page_title="RambuVision — Ensiklopedia", page_icon="📖", layout="wide")
inject_global_css()

with st.sidebar:
    sidebar_brand()
    st.page_link("app.py", label="Deteksi Rambu")
    st.page_link("pages/1_Ensiklopedia_Rambu.py", label="Ensiklopedia Rambu")
    st.page_link("pages/2_Statistik_Model.py", label="Statistik Model")
    st.page_link("pages/3_Galeri_Deteksi.py", label="Galeri Deteksi")
    st.page_link("pages/4_Tentang_Proyek.py", label="Tentang Proyek")

eyebrow("Referensi Rambu")
st.title("Ensiklopedia 5 Rambu")
st.write("Ketahui arti, bentuk, dan aturan dari setiap rambu yang dikenali sistem ini.")

RAMBU_DATA = [
    {
        "no": "01",
        "nama": "Larangan Memutar Balik",
        "kategori": "Rambu Larangan",
        "bentuk": "Bundar, dasar putih, garis tepi & diagonal merah",
        "arti": "Pengendara dilarang melakukan putar balik (U-turn) pada ruas jalan ini.",
        "lokasi_umum": "Jalan dua arah dengan median, area rawan kecelakaan akibat putar balik.",
    },
    {
        "no": "02",
        "nama": "Penyeberangan Pejalan Kaki",
        "kategori": "Rambu Petunjuk",
        "bentuk": "Bujur sangkar, dasar biru dengan simbol orang menyeberang di zebra cross",
        "arti": "Menandakan adanya lintasan penyeberangan pejalan kaki di depan. Pengendara wajib mengurangi laju dan memberi prioritas pada pejalan kaki.",
        "lokasi_umum": "Dekat sekolah, pasar, halte, dan kawasan permukiman padat.",
    },
    {
        "no": "03",
        "nama": "Larangan Berhenti",
        "kategori": "Rambu Larangan",
        "bentuk": "Bundar, dasar biru dengan garis silang merah",
        "arti": "Kendaraan dilarang berhenti, termasuk berhenti sementara, di sepanjang ruas yang ditandai.",
        "lokasi_umum": "Depan fasilitas umum, jalur cepat, dan tikungan tajam.",
    },
    {
        "no": "04",
        "nama": "Simpang Tiga",
        "kategori": "Rambu Peringatan",
        "bentuk": "Segitiga, dasar kuning dengan simbol pertigaan",
        "arti": "Memperingatkan pengendara akan adanya pertigaan jalan di depan, agar lebih waspada dan menyesuaikan kecepatan.",
        "lokasi_umum": "Sebelum titik pertemuan tiga ruas jalan.",
    },
    {
        "no": "05",
        "nama": "Simpang Empat",
        "kategori": "Rambu Peringatan",
        "bentuk": "Segitiga, dasar kuning dengan simbol perempatan",
        "arti": "Memperingatkan pengendara akan adanya perempatan jalan di depan, agar lebih waspada dan menyesuaikan kecepatan.",
        "lokasi_umum": "Sebelum titik pertemuan empat ruas jalan.",
    },
]

for rambu in RAMBU_DATA:
    st.markdown(
        f"""
        <div class="rambu-card">
            <div style="display:flex; gap:1.4rem; align-items:flex-start;">
                <div style="font-family:'JetBrains Mono',monospace; font-size:1.8rem; font-weight:700;
                            color:{GOLD}; opacity:0.5; min-width:3rem; line-height:1;">{rambu['no']}</div>
                <div style="flex:1;">
                    <div style="font-family:'JetBrains Mono',monospace; font-size:0.7rem; letter-spacing:0.08em;
                                text-transform:uppercase; color:{GOLD};">{rambu['kategori']}</div>
                    <div style="font-family:'Fraunces',serif; font-size:1.35rem; font-weight:700; margin:0.15rem 0 0.6rem 0;">
                        {rambu['nama']}
                    </div>
                    <p style="margin:0 0 0.5rem 0;"><strong>Bentuk &amp; warna:</strong> {rambu['bentuk']}</p>
                    <p style="margin:0 0 0.5rem 0;"><strong>Arti:</strong> {rambu['arti']}</p>
                    <p style="margin:0; opacity:0.75;"><strong>Umum ditemukan di:</strong> {rambu['lokasi_umum']}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
