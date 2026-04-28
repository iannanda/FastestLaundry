import streamlit as st
import os

st.set_page_config(layout="wide")

# ─── CUSTOM CSS ─────────────────────────────────────────────
st.markdown("""
<style>
body {
    background: #f5f7fb;
}

.navbar {
    background: linear-gradient(90deg,#0ea5e9,#0284c7);
    padding: 15px 30px;
    border-radius: 10px;
    color: white;
    font-weight: bold;
}

.hero {
    background: linear-gradient(135deg,#0ea5e9,#0369a1);
    padding: 50px;
    border-radius: 20px;
    color: white;
    margin-top: 20px;
}

.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    text-align: center;
}

.service-card {
    background: #f1f5f9;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #cbd5e1;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ─── NAVBAR ─────────────────────────────────────────────
st.markdown("""
<div class="navbar">
    🌊 CleanWave &nbsp;&nbsp;&nbsp;
    🏠 Beranda &nbsp;&nbsp;
    📦 Pesan &nbsp;&nbsp;
    📋 Riwayat &nbsp;&nbsp;
    ⭐ Member &nbsp;&nbsp;
    🔧 Alat &nbsp;&nbsp;
    👤 Masuk
</div>
""", unsafe_allow_html=True)

# ─── HERO SECTION ────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>CleanWave Laundry 🌊</h1>
    <p>Layanan laundry profesional dengan sistem digital terintegrasi.</p>
    <button style="padding:10px 20px;border:none;border-radius:10px;background:#0284c7;color:white;">Pesan Sekarang</button>
</div>
""", unsafe_allow_html=True)

# ─── STAT CARD ───────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><h2>3</h2><p>Pelanggan</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h2>5</h2><p>Transaksi</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h2>1</h2><p>Member Gold</p></div>', unsafe_allow_html=True)

# ─── LAYANAN ─────────────────────────────────────────────
st.markdown("## Layanan Kami")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="service-card">
        <h4>Cuci & Setrika</h4>
        <p>Rp 10.000/kg</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="service-card">
        <h4>Setrika Saja</h4>
        <p>Rp 7.000/kg</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <h4>Cuci Kering</h4>
        <p>Rp 8.000/kg</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="service-card">
        <h4>Express</h4>
        <p>Rp 15.000/kg</p>
    </div>
    """, unsafe_allow_html=True)
