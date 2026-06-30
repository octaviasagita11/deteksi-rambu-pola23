"""
style.py — Modul styling bersama untuk seluruh halaman aplikasi
Deteksi Rambu Lalu Lintas Indonesia.

Tema: Navy & Cream — TANPA ikon/SVG, murni tipografi dan warna sebagai aksen.
"""

import streamlit as st

NAVY_DARK = "#0B1F3A"
NAVY_MID = "#16335C"
NAVY_LIGHT = "#234070"
CREAM = "#F5EFE0"
CREAM_DIM = "#C9C2AE"
GOLD = "#D4A857"
OLIVE = "#2E7D5B"
TERRACOTTA = "#B5483D"


def inject_global_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
        }}

        .stApp {{
            background: {NAVY_DARK};
            color: {CREAM};
        }}

        section[data-testid="stSidebar"] {{
            background: {NAVY_MID};
            border-right: 1px solid {NAVY_LIGHT};
        }}
        section[data-testid="stSidebar"] * {{
            color: {CREAM} !important;
        }}
        section[data-testid="stSidebar"] hr {{
            border-color: {NAVY_LIGHT};
        }}

        h1, h2, h3 {{
            font-family: 'Fraunces', serif;
            color: {CREAM};
            letter-spacing: -0.01em;
        }}
        h1 {{ font-weight: 700; }}
        h2 {{ font-weight: 600; }}

        .eyebrow {{
            display: inline-block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: {GOLD};
            margin-bottom: 0.4rem;
            border-bottom: 1px solid {GOLD};
            padding-bottom: 0.3rem;
        }}

        .rambu-card {{
            background: {NAVY_MID};
            border: 1px solid {NAVY_LIGHT};
            border-radius: 14px;
            padding: 1.4rem 1.6rem;
            margin-bottom: 1rem;
        }}
        .rambu-card-gold {{
            background: {NAVY_MID};
            border: 1px solid {GOLD};
            border-left: 4px solid {GOLD};
            border-radius: 10px;
            padding: 1.2rem 1.4rem;
            margin-bottom: 1rem;
        }}

        .stat-tile {{
            background: {NAVY_MID};
            border: 1px solid {NAVY_LIGHT};
            border-radius: 12px;
            padding: 1.1rem 1.3rem;
            text-align: left;
        }}
        .stat-tile .stat-label {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: {CREAM_DIM};
        }}
        .stat-tile .stat-value {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 2rem;
            font-weight: 700;
            color: {GOLD};
            line-height: 1.2;
        }}
        .stat-tile .stat-sub {{
            font-size: 0.78rem;
            color: {CREAM_DIM};
            margin-top: 0.15rem;
        }}

        .badge-success {{
            display: inline-block;
            background: rgba(46,125,91,0.18);
            color: {OLIVE};
            border: 1px solid {OLIVE};
            border-radius: 999px;
            padding: 0.25rem 0.85rem;
            font-size: 0.82rem;
            font-weight: 600;
        }}
        .badge-warning {{
            display: inline-block;
            background: rgba(181,72,61,0.18);
            color: #E08A7D;
            border: 1px solid {TERRACOTTA};
            border-radius: 999px;
            padding: 0.25rem 0.85rem;
            font-size: 0.82rem;
            font-weight: 600;
        }}

        /* Sign row — versi tipografi murni, tanpa ikon */
        .sign-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.8rem;
            background: {NAVY_LIGHT};
            border-left: 3px solid {GOLD};
            border-radius: 6px;
            padding: 0.6rem 1rem;
            margin-bottom: 0.5rem;
        }}
        .sign-row .sign-index {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            color: {GOLD};
            letter-spacing: 0.08em;
            min-width: 1.6rem;
        }}
        .sign-row .sign-name {{
            flex: 1;
            font-weight: 600;
            font-size: 0.95rem;
        }}
        .sign-row .sign-score {{
            font-family: 'JetBrains Mono', monospace;
            color: {GOLD};
            font-size: 0.88rem;
        }}

        .thin-divider {{
            height: 1px;
            background: linear-gradient(90deg, {GOLD}, transparent);
            margin: 1.4rem 0;
            border: none;
        }}

        .stButton > button, .stDownloadButton > button {{
            background: {GOLD};
            color: {NAVY_DARK};
            border: none;
            border-radius: 8px;
            font-weight: 600;
            padding: 0.55rem 1.4rem;
        }}
        .stButton > button:hover, .stDownloadButton > button:hover {{
            background: #E3BC72;
            color: {NAVY_DARK};
        }}

        [data-testid="stFileUploaderDropzone"] {{
            background: {NAVY_MID};
            border: 1.5px dashed {GOLD};
            border-radius: 12px;
        }}

        [data-testid="stSlider"] [role="slider"] {{
            background-color: {GOLD};
        }}

        button[data-baseweb="tab"] {{
            color: {CREAM_DIM};
            font-family: 'Inter', sans-serif;
            font-weight: 600;
        }}
        button[data-baseweb="tab"][aria-selected="true"] {{
            color: {GOLD};
        }}

        [data-testid="stDataFrame"] {{
            border-radius: 10px;
            overflow: hidden;
        }}

        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        [data-testid="stSidebarNav"] {{ display: none; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def eyebrow(text: str):
    st.markdown(f'<div class="eyebrow">{text}</div>', unsafe_allow_html=True)


def stat_tile(label: str, value: str, sub: str = ""):
    st.markdown(
        f"""
        <div class="stat-tile">
            <div class="stat-label">{label}</div>
            <div class="stat-value">{value}</div>
            <div class="stat-sub">{sub}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def sign_row(index_label: str, name: str, score: str = ""):
    """Baris tipografi murni untuk menampilkan nama rambu, tanpa ikon."""
    score_html = f'<span class="sign-score">{score}</span>' if score else ""
    st.markdown(
        f"""
        <div class="sign-row">
            <span class="sign-index">{index_label}</span>
            <span class="sign-name">{name}</span>
            {score_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def sidebar_brand():
    st.markdown(
        f"""
        <div style="padding: 0.6rem 0 1.2rem 0; border-bottom: 1px solid {NAVY_LIGHT}; margin-bottom: 1.2rem;">
            <div style="font-family:'Fraunces',serif; font-weight:700; font-size:1.3rem; line-height:1.1; color:{CREAM};">
                Rambu<span style="color:{GOLD};">Vision</span>
            </div>
            <div style="font-family:'JetBrains Mono',monospace; font-size:0.66rem; color:{CREAM_DIM}; letter-spacing:0.08em; margin-top:0.2rem;">
                FASTER R-CNN &middot; INDONESIA
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
