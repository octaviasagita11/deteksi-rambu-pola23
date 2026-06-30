import os
import requests
import streamlit as st
import torch

@st.cache_resource
def ambil_model_gdrive():
    # Ubah link share biasa menjadi link direct download gdrive
    # Kamu bisa gunakan format: https://id.gdrive.vip/ atau ganti id-nya langsung
    url = "https://drive.google.com/file/d/1j_UWMfeyxVeHDELjh6jHdxdgRbMjDMkB/view?usp=sharing"
    model_name = "model_rambu_full.pth"
    
    # Jika file belum ada di server Streamlit, download dulu
    if not os.path.exists(model_name):
        with st.spinner("Sedang mengunduh file model dari Google Drive (160MB), mohon tunggu..."):
            response = requests.get(url)
            with open(model_name, "wb") as f:
                f.write(response.content)
    return model_name

# --- BAGIAN LOAD MODEL KAMU ---
# Panggil fungsi di atas untuk mendapatkan path modelnya
path_model_terunduh = ambil_model_gdrive()

# Gunakan path tersebut di torch.load kamu, pastikan pakai map_location='cpu'
# Contoh:
# model = ArsitekturModelKamu()
# model.load_state_dict(torch.load(path_model_terunduh, map_location=torch.device('cpu')))