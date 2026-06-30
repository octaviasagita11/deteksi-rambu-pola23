import os
import requests
import streamlit as st
import torch

# 1. Tambahkan fungsi unduh otomatis ini di bagian atas app.py
@st.cache_resource
def ambil_model_gdrive():
    # GANTI LINK INI dengan link direct download Google Drive milikmu!
    url = "https://drive.google.com/file/d/1j_UWMfeyxVeHDELjh6jHdxdgRbMjDMkB/view?usp=sharing" 
    model_name = "model_rambu_full.pth"
    
    if not os.path.exists(model_name):
        with st.spinner("Sedang mengunduh file model dari Google Drive (160MB), mohon tunggu..."):
            response = requests.get(url)
            with open(model_name, "wb") as f:
                f.write(response.content)
    return model_name

# 2. Cari baris torch.load kamu yang lama, lalu sesuaikan seperti ini:
path_model_terunduh = ambil_model_gdrive()

# Contoh penerapan pada inisialisasi model kamu:
# model = NamaArsitekturModelKamu()
# model.load_state_dict(torch.load(path_model_terunduh, map_location=torch.device('cpu')))