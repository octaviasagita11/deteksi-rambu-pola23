import os
import requests
import streamlit as st
import torch

# PENTING: Taruh teks judul di paling atas agar kamu tahu aplikasinya bekerja atau tidak!
st.title("Aplikasi Deteksi Rambu Lalu Lintas")
st.write("Memulai inisialisasi aplikasi...")

@st.cache_resource
def ambil_model_gdrive_robust():
    file_id = "1j_UWMfeyxVeHDELjh6jHdxdgRbMjDMkB"
    model_name = "model_rambu_full.pth"
    
    if os.path.exists(model_name):
        return model_name
        
    # Jika file belum ada, mulai proses unduh dengan penanganan file besar
    status_text = st.empty()
    status_text.info("Menghubungkan ke Google Drive untuk mengunduh model (160MB)...")
    
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    
    # Request pertama untuk mendapatkan halaman/token konfirmasi virus
    response = session.get(URL, params={'id': file_id}, stream=True)
    
    # Fungsi internal untuk mendapatkan token konfirmasi
    def get_confirm_token(res):
        for key, value in res.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None

    token = get_confirm_token(response)
    
    # Jika Google meminta konfirmasi file besar, kirim balik tokennya
    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)
        
    # Mulai mengunduh file biner asli
    status_text.warning("Sedang mengunduh file model. Mohon tunggu, jangan tutup halaman ini...")
    
    try:
        with open(model_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=32768):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        status_text.success("Model berhasil diunduh dan siap digunakan!")
    except Exception as e:
        status_text.error(f"Gagal mengunduh model: {e}")
        
    return model_name

# Eksekusi fungsi pengunduh yang baru
path_model_terunduh = ambil_model_gdrive_robust()

# --- LANJUTAN KODE ARSITEKTUR & LOAD MODEL KAMU ---
# model = NamaArsitekturModelKamu()
# model.load_state_dict(torch.load(path_model_terunduh, map_location=torch.device('cpu')))