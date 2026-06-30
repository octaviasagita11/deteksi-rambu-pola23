import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from style import inject_global_css, sidebar_brand, eyebrow, stat_tile, GOLD, OLIVE, TERRACOTTA, NAVY_DARK, NAVY_MID, CREAM, CREAM_DIM

st.set_page_config(page_title="RambuVision — Statistik", page_icon="📊", layout="wide")
inject_global_css()

with st.sidebar:
    sidebar_brand()
    st.page_link("app.py", label="Deteksi Rambu")
    st.page_link("pages/1_Ensiklopedia_Rambu.py", label="Ensiklopedia Rambu")
    st.page_link("pages/2_Statistik_Model.py", label="Statistik Model")
    st.page_link("pages/3_Galeri_Deteksi.py", label="Galeri Deteksi")
    st.page_link("pages/4_Tentang_Proyek.py", label="Tentang Proyek")

eyebrow("Performa Model")
st.title("Statistik Evaluasi")
st.write("Hasil evaluasi model pada 135 gambar data uji yang belum pernah dilihat selama pelatihan.")

c1, c2, c3 = st.columns(3)
with c1:
    stat_tile("mAP @ 0.50", "0.9919", "IoU longgar — standar PASCAL VOC")
with c2:
    stat_tile("mAP @ 0.50:0.95", "0.7715", "IoU ketat — standar COCO")
with c3:
    stat_tile("Total Data Uji", "135", "gambar, 5 kelas rambu")

st.markdown('<hr class="thin-divider">', unsafe_allow_html=True)

st.subheader("Precision, Recall & F1-Score per Kelas")

data_metrik = {
    'Kelas': ['Larangan Memutar Balik', 'Penyeberangan Pejalan Kaki',
              'Larangan Berhenti', 'Simpang Tiga', 'Simpang Empat'],
    'Precision': [1.0000, 1.0000, 0.9615, 0.9189, 1.0000],
    'Recall': [0.9630, 1.0000, 1.0000, 1.0000, 1.0000],
    'F1-Score': [0.9811, 1.0000, 0.9804, 0.9577, 1.0000],
}
df = pd.DataFrame(data_metrik)

col_table, col_chart = st.columns([1, 1.2], gap="large")

with col_table:
    st.dataframe(
        df.style.format({'Precision': '{:.2%}', 'Recall': '{:.2%}', 'F1-Score': '{:.2%}'})
        .background_gradient(cmap='YlOrBr', subset=['Precision', 'Recall', 'F1-Score'], vmin=0.85, vmax=1.0),
        use_container_width=True,
        hide_index=True,
    )
    st.caption(
        "Tidak ada kelas yang mencapai 0% — performa tersebar wajar di seluruh kelas, "
        "tanda model belajar dari data yang representatif."
    )

with col_chart:
    fig, ax = plt.subplots(figsize=(7, 4.2))
    fig.patch.set_facecolor(NAVY_DARK)
    ax.set_facecolor(NAVY_DARK)

    x = np.arange(len(df['Kelas']))
    width = 0.25
    ax.bar(x - width, df['Precision'], width, label='Precision', color=GOLD)
    ax.bar(x, df['Recall'], width, label='Recall', color=OLIVE)
    ax.bar(x + width, df['F1-Score'], width, label='F1-Score', color='#7A8FB8')

    ax.set_ylim(0, 1.15)
    ax.set_xticks(x)
    ax.set_xticklabels([c.replace(' ', '\n') for c in df['Kelas']], fontsize=8, color=CREAM)
    ax.tick_params(colors=CREAM)
    for spine in ax.spines.values():
        spine.set_color(NAVY_MID)
    ax.legend(facecolor=NAVY_MID, edgecolor='none', labelcolor=CREAM, fontsize=8)
    ax.grid(axis='y', alpha=0.15, color=CREAM)
    plt.tight_layout()
    st.pyplot(fig)

st.markdown('<hr class="thin-divider">', unsafe_allow_html=True)

st.subheader("Confusion Matrix")
tab1, tab2 = st.tabs(["Matrix Gabungan", "Per Kelas (TP / FP / FN)"])

classes_only = ['Memutar\nBalik', 'Penyeberangan', 'Larangan\nBerhenti', 'Simpang\nTiga', 'Simpang\nEmpat']

with tab1:
    cm = np.array([
        [26, 0, 0, 0, 0],
        [0, 25, 0, 0, 0],
        [0, 0, 25, 0, 0],
        [0, 0, 0, 34, 0],
        [0, 0, 0, 0, 25],
    ])
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    fig.patch.set_facecolor(NAVY_DARK)
    cmap_navy = sns.light_palette(GOLD, as_cmap=True)
    sns.heatmap(cm, annot=True, fmt='d', cmap=cmap_navy, ax=ax,
                xticklabels=classes_only, yticklabels=classes_only,
                cbar_kws={'label': 'Jumlah'}, linewidths=0.5, linecolor=NAVY_MID)
    ax.set_xlabel('Prediksi Model', color=CREAM)
    ax.set_ylabel('Label Sebenarnya', color=CREAM)
    ax.tick_params(colors=CREAM)
    plt.tight_layout()
    st.pyplot(fig)
    st.caption(
        "Diagonal sempurna berarti model tidak pernah tertukar antar kelas. "
        "Matrix ini hanya menghitung objek yang berhasil match (IoU ≥ 0.5) — "
        "kasus gagal deteksi atau false alarm tidak tercermin di sini."
    )

with tab2:
    detail = {
        'Larangan Memutar Balik': {'TP': 26, 'FP': 0, 'FN': 1},
        'Penyeberangan Pejalan Kaki': {'TP': 25, 'FP': 0, 'FN': 0},
        'Larangan Berhenti': {'TP': 25, 'FP': 1, 'FN': 0},
        'Simpang Tiga': {'TP': 34, 'FP': 3, 'FN': 0},
        'Simpang Empat': {'TP': 25, 'FP': 0, 'FN': 0},
    }
    cols = st.columns(len(detail))
    for col, (nama, d) in zip(cols, detail.items()):
        with col:
            st.markdown(f"**{nama}**")
            st.markdown(
                f"""<div class="rambu-card" style="padding:0.9rem 1rem;">
                <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
                    <span style="color:{CREAM_DIM};">TP</span><span style="color:{OLIVE}; font-weight:700;">{d['TP']}</span>
                </div>
                <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
                    <span style="color:{CREAM_DIM};">FP</span><span style="color:{TERRACOTTA}; font-weight:700;">{d['FP']}</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span style="color:{CREAM_DIM};">FN</span><span style="color:{TERRACOTTA}; font-weight:700;">{d['FN']}</span>
                </div>
                </div>""",
                unsafe_allow_html=True,
            )
    st.caption(
        "TP = terdeteksi benar · FP = salah deteksi (false alarm) · FN = rambu asli yang terlewat (miss detection)."
    )

st.markdown('<hr class="thin-divider">', unsafe_allow_html=True)

st.subheader("Kurva Training")
epochs = list(range(1, 31))
train_loss = [0.1906, 0.1041, 0.0904, 0.0793, 0.0726, 0.0680, 0.0662, 0.0627, 0.0596, 0.0575,
              0.0490, 0.0469, 0.0467, 0.0449, 0.0449, 0.0442, 0.0441, 0.0435, 0.0444, 0.0431,
              0.0421, 0.0417, 0.0425, 0.0421, 0.0410, 0.0415, 0.0420, 0.0428, 0.0424, 0.0430]
val_loss = [0.1265, 0.0861, 0.0875, 0.0787, 0.0726, 0.0748, 0.0783, 0.0654, 0.0648, 0.0634,
            0.0552, 0.0533, 0.0539, 0.0530, 0.0539, 0.0552, 0.0523, 0.0531, 0.0526, 0.0546,
            0.0537, 0.0536, 0.0524, 0.0524, 0.0530, 0.0531, 0.0529, 0.0534, 0.0528, 0.0533]

fig, ax = plt.subplots(figsize=(11, 4))
fig.patch.set_facecolor(NAVY_DARK)
ax.set_facecolor(NAVY_DARK)
ax.plot(epochs, train_loss, label='Train Loss', color=GOLD, linewidth=2)
ax.plot(epochs, val_loss, label='Validation Loss', color='#7A8FB8', linewidth=2)
ax.axvline(17, color=OLIVE, linestyle='--', linewidth=1.2, alpha=0.7)
ax.text(17.3, 0.16, 'Model terbaik\n(epoch 17)', color=OLIVE, fontsize=8)
ax.set_xlabel('Epoch', color=CREAM)
ax.set_ylabel('Loss', color=CREAM)
ax.tick_params(colors=CREAM)
for spine in ax.spines.values():
    spine.set_color(NAVY_MID)
ax.legend(facecolor=NAVY_MID, edgecolor='none', labelcolor=CREAM)
ax.grid(alpha=0.15, color=CREAM)
plt.tight_layout()
st.pyplot(fig)
st.caption(
    "Model mencapai val loss terendah di epoch 17, lalu konvergen (mendatar) hingga epoch 30 — "
    "menandakan kapasitas belajar dari data yang ada sudah optimal dimanfaatkan."
)
