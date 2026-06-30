import os
import requests
import streamlit as st
import torch

@st.cache_resource
def ambil_model_gdrive():
    # Menggunakan ID file dari link Google Drive kamu
    file_id = "1j_UWMfeyxVeHDELjh6jHdxdgRbMjDMkB"
    # Menggunakan endpoint download khusus untuk memicu direct download file besar
    url = f"https://docs.google.com/uc?export=download&id={file_id}&confirm=t"
    model_name = "model_rambu_full.pth"
    
    if not os.path.exists(model_name):
        with st.spinner("Sedang mengunduh file model dari Google Drive (160MB), mohon tunggu sebentar..."):
            # Menggunakan stream=True agar download file besar lebih stabil dan aman
            with requests.get(url, stream=True) as response:
                response.raise_for_status()
                with open(model_name, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
    return model_name

# Panggil fungsi download otomatis
path_model_terunduh = ambil_model_gdrive()

# SENSOR / CONTOH LOAD MODEL (Sesuaikan dengan nama variabel model & arsitektur asli kamu di bawah ini):
# model = NamaArsitekturModelKamu()
# model.load_state_dict(torch.load(path_model_terunduh, map_location=torch.device('cpu')))