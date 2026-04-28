import streamlit as st
from datetime import date
import pandas as pd
import json
import os

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CleanWave Laundry",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── LOAD CSS ─────────────────────────────────────────────────────────────────
def load_css():
    with open(os.path.join(os.path.dirname(__file__), "style.css")) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ─── DATA DEFAULTS ────────────────────────────────────────────────────────────
DEFAULT_CUSTOMERS = [
    {"id": 1, "nama": "Budi Santoso",  "hp": "081234567890", "email": "budi@email.com",  "bergabung": "2024-01-10", "poin": 320, "tier": "Silver"},
    {"id": 2, "nama": "Siti Rahayu",   "hp": "082345678901", "email": "siti@email.com",  "bergabung": "2024-02-15", "poin": 750, "tier": "Gold"},
    {"id": 3, "nama": "Ahmad Fauzi",   "hp": "083456789012", "email": "ahmad@email.com", "bergabung": "2024-03-20", "poin": 120, "tier": "Bronze"},
]

DEFAULT_TRANSAKSI = [
    {"id": 1001, "customer_id": 1, "tanggal": "2025-04-01", "kg": 3.5, "layanan": "Cuci & Setrika",  "harga": 35000, "status": "Selesai",   "poin": 35, "deterjen": "Attack",       "mesin": "Mesin LG 9kg"},
    {"id": 1002, "customer_id": 2, "tanggal": "2025-04-05", "kg": 5.0, "layanan": "Cuci Kering",     "harga": 40000, "status": "Selesai",   "poin": 40, "deterjen": "Rinso",        "mesin": "Mesin Samsung 10kg"},
    {"id": 1003, "customer_id": 1, "tanggal": "2025-04-10", "kg": 2.0, "layanan": "Setrika Saja",    "harga": 14000, "status": "Diproses",  "poin": 14, "deterjen": "-",            "mesin": "Setrika Uap Philips"},
    {"id": 1004, "customer_id": 3, "tanggal": "2025-04-12", "kg": 4.0, "layanan": "Cuci & Setrika",  "harga": 40000, "status": "Selesai",   "poin": 40, "deterjen": "Daia",         "mesin": "Mesin LG 9kg"},
    {"id": 1005, "customer_id": 2, "tanggal": "2025-04-15", "kg": 6.5, "layanan": "Cuci Kering",     "harga": 52000, "status": "Menunggu",  "poin": 52, "deterjen": "Attack",       "mesin": "Mesin Samsung 10kg"},
]

LAYANAN = {
    "Cuci & Setrika":  {"harga_per_kg": 10000, "deskripsi": "Dicuci bersih + disetrika rapi"},
    "Cuci Kering":     {"harga_per_kg": 8000,  "deskripsi": "Dicuci + dikeringkan mesin"},
    "Setrika Saja":    {"harga_per_kg": 7000,  "deskripsi": "Hanya layanan setrika"},
    "Express (6 jam)": {"harga_per_kg": 15000, "deskripsi": "Selesai dalam 6 jam, cuci + setrika"},
}

HADIAH = [
    {"nama": "Diskon 10%",     "poin": 100, "icon": "🏷️", "deskripsi": "Diskon 10% untuk transaksi berikutnya"},
    {"nama": "Gratis Cuci 2kg","poin": 250, "icon": "👕", "deskripsi": "Gratis layanan cuci hingga 2kg"},
    {"nama": "Gratis Setrika", "poin": 150, "icon": "🔥", "deskripsi": "Gratis layanan setrika untuk satu order"},
    {"nama": "Diskon 25%",     "poin": 400, "icon": "💎", "deskripsi": "Diskon besar 25% untuk transaksi berikutnya"},
    {"nama": "Gratis Cuci 5kg","poin": 600, "icon": "🎁", "deskripsi": "Gratis layanan cuci hingga 5kg"},
]

PERALATAN = [
    {"kategori": "Mesin Cuci", "nama": "LG Front Load 9kg",       "brand": "LG",      "kapasitas": "9 kg",  "deskripsi": "Cocok untuk pakaian sehari-hari, program cuci hemat energi", "icon": "🫧"},
    {"kategori": "Mesin Cuci", "nama": "Samsung Top Load 10kg",   "brand": "Samsung", "kapasitas": "10 kg", "deskripsi": "Kapasitas besar untuk cucian keluarga, teknologi eco-bubble",  "icon": "🫧"},
    {"kategori": "Pengering",  "nama": "Dryer LG 8kg",            "brand": "LG",      "kapasitas": "8 kg",  "deskripsi": "Pengeringan cepat dengan sensor kelembaban otomatis",          "icon": "💨"},
    {"kategori": "Setrika",    "nama": "Setrika Uap Philips GC2672","brand": "Philips","kapasitas": "-",    "deskripsi": "Setrika uap tekanan tinggi, anti kusut sempurna",              "icon": "♨️"},
]

BAHAN = [
    {"nama": "Attack",            "tipe": "Deterjen",  "kegunaan": "Cuci standar",        "icon": "🧴", "cocok": "Semua jenis kain"},
    {"nama": "Rinso Anti Noda",   "tipe": "Deterjen",  "kegunaan": "Noda membandel",      "icon": "🧴", "cocok": "Katun, polyester"},
    {"nama": "Daia Bunga",        "tipe": "Deterjen",  "kegunaan": "Pewangi kuat",        "icon": "🧴", "cocok": "Semua jenis kain"},
    {"nama": "Molto Konsentrat",  "tipe": "Pelembut",  "kegunaan": "Pelembut & pewangi",  "icon": "🌸", "cocok": "Semua kain"},
    {"nama": "So Klin Pemutih",   "tipe": "Pemutih",   "kegunaan": "Pakaian putih",       "icon": "⚪", "cocok": "Hanya kain putih"},
    {"nama": "Air RO",            "tipe": "Air",       "kegunaan": "Air bersih proses cuci","icon": "💧","cocok": "Semua laundry"},
]

# ─── SESSION STATE ─────────────────────────────────────────────────────────────
def init_state():
    if "customers" not in st.session_state:
        st.session_state.customers = DEFAULT_CUSTOMERS.copy()
    if "transaksi" not in st.session_state:
        st.session_state.transaksi = DEFAULT_TRANSAKSI.copy()
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = None
    if "page" not in st.session_state:
        st.session_state.page = "Beranda"
    if "notif" not in st.session_state:
        st.session_state.notif = None

init_state()

# ─── HELPERS ──────────────────────────────────────────────────────────────────
def get_tier(poin):
    if poin >= 500: return "Gold",   "#F59E0B", "🥇"
    if poin >= 200: return "Silver", "#6B7280", "🥈"
    return "Bronze", "#92400E", "🥉"

def format_rp(val):
    return f"Rp {int(val):,}".replace(",", ".")

def find_customer(customer_id):
    return next((c for c in st.session_state.customers if c["id"] == customer_id), None)

def next_tx_id():
    if not st.session_state.transaksi:
        return 1001
    return max(t["id"] for t in st.session_state.transaksi) + 1

def update_customer_points(customer_id, tambah_poin):
    for i, c in enumerate(st.session_state.customers):
        if c["id"] == customer_id:
            new_poin = c["poin"] + tambah_poin
            tier_name, _, _ = get_tier(new_poin)
            st.session_state.customers[i] = {**c, "poin": new_poin, "tier": tier_name}
            if st.session_state.logged_in and st.session_state.logged_in["id"] == customer_id:
                st.session_state.logged_in = st.session_state.customers[i]
            break

def show_notif(msg, tipe="success"):
    if tipe == "success":
        st.success(msg)
    else:
        st.error(msg)

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">🌊 CleanWave Laundry</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">Sistem Manajemen Laundry Digital</div>', unsafe_allow_html=True)
    st.markdown("---")

    if st.session_state.logged_in:
        u = st.session_state.logged_in
        tier_name, tier_color, tier_icon = get_tier(u["poin"])
        st.markdown(f"""
        <div class="member-card">
            <div class="member-name">👤 {u['nama']}</div>
            <div class="member-info">{u['hp']}</div>
            <div class="member-points">⭐ {u['poin']} Poin</div>
            <div class="member-tier">{tier_icon} {tier_name} Member</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("")

    menu_items = ["🏠 Beranda", "📦 Pesan Laundry", "📋 Riwayat Transaksi", "⭐ Membership", "🔧 Alat & Bahan"]
    if st.session_state.logged_in:
        menu_items.append("👤 Profil Saya")
    else:
        menu_items.append("🔑 Masuk / Daftar")

    selected = st.radio("Navigasi", menu_items, label_visibility="collapsed")
    page = selected.split(" ", 1)[1]
    st.session_state.page = page

    st.markdown("---")
    if st.session_state.logged_in:
        if st.button("🚪 Keluar", use_container_width=True):
            st.session_state.logged_in = None
            st.session_state.page = "Beranda"
            st.rerun()

    st.markdown('<div class="sidebar-footer">Industry 4.0 Prototype · UMKM Laundry</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: BERANDA
# ══════════════════════════════════════════════════════════════════════════════
if page == "Beranda":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">UMKM LAUNDRY · INDUSTRY 4.0 READY</div>
        <h1 class="hero-title">CleanWave Laundry 🌊</h1>
        <p class="hero-desc">Layanan laundry profesional dengan sistem digital terintegrasi.<br>Titip baju, kami urus semuanya.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    total_tx     = len(st.session_state.transaksi)
    total_cust   = len(st.session_state.customers)
    total_gold   = sum(1 for c in st.session_state.customers if c["tier"] == "Gold")
    total_omset  = sum(t["harga"] for t in st.session_state.transaksi)

    with col1:
        st.markdown(f'<div class="stat-card"><div class="stat-icon">👥</div><div class="stat-val">{total_cust}</div><div class="stat-label">Pelanggan Aktif</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stat-card"><div class="stat-icon">📦</div><div class="stat-val">{total_tx}</div><div class="stat-label">Total Transaksi</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="stat-card"><div class="stat-icon">⭐</div><div class="stat-val">{total_gold}</div><div class="stat-label">Member Gold</div></div>', unsafe_allow_html=True)

    st.markdown("### 🧺 Layanan Kami")
    col1, col2 = st.columns(2)
    layanan_list = list(LAYANAN.items())
    for i, (nama, info) in enumerate(layanan_list):
        with (col1 if i % 2 == 0 else col2):
            st.markdown(f"""
            <div class="service-card">
                <div class="service-name">{nama}</div>
                <div class="service-desc">{info['deskripsi']}</div>
                <div class="service-price">{format_rp(info['harga_per_kg'])}<span class="service-unit">/kg</span></div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### 💡 Program Membership")
    st.markdown("""
    <div class="promo-banner">
        <span style="font-size:2rem">⭐</span>
        <div style="flex:1">
            <b style="font-size:1.1rem">Kumpulkan Poin, Dapatkan Hadiah!</b><br>
            Setiap Rp 1.000 yang Anda keluarkan = 1 poin. Tukarkan poin dengan diskon & layanan gratis!
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: PESAN LAUNDRY
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Pesan Laundry":
    st.markdown("## 📦 Pesan Laundry")
    st.markdown("Isi formulir di bawah untuk menitipkan laundry Anda.")

    col_form, col_sum = st.columns([1.4, 1])

    with col_form:
        with st.container(border=True):
            st.markdown("#### 👤 Data Pelanggan")
            nama  = st.text_input("Nama Lengkap", value=st.session_state.logged_in["nama"] if st.session_state.logged_in else "")
            hp    = st.text_input("Nomor HP", value=st.session_state.logged_in["hp"] if st.session_state.logged_in else "", placeholder="08xxxxxxxxxx")

        with st.container(border=True):
            st.markdown("#### 🧺 Pilih Layanan")
            layanan_pilihan = st.radio(
                "Layanan",
                list(LAYANAN.keys()),
                label_visibility="collapsed",
                format_func=lambda x: f"{x} — {format_rp(LAYANAN[x]['harga_per_kg'])}/kg"
            )
            st.caption(f"📝 {LAYANAN[layanan_pilihan]['deskripsi']}")

        with st.container(border=True):
            st.markdown("#### ⚖️ Detail Cucian")
            kg = st.number_input("Berat Pakaian (kg)", min_value=0.5, max_value=50.0, value=1.0, step=0.5)
            catatan = st.text_area("Catatan (opsional)", placeholder="Alergi deterjen tertentu, pakaian khusus, dll.", height=80)

    with col_sum:
        harga_per_kg = LAYANAN[layanan_pilihan]["harga_per_kg"]
        total = int(kg * harga_per_kg)
        poin_dapat = total // 1000

        with st.container(border=True):
            st.markdown("#### 🧾 Ringkasan Pesanan")
            st.markdown(f"""
            | Item | Detail |
            |------|--------|
            | Layanan | {layanan_pilihan} |
            | Harga/kg | {format_rp(harga_per_kg)} |
            | Berat | {kg} kg |
            """)
            st.markdown(f"<div class='total-box'><span>Total</span><b>{format_rp(total)}</b></div>", unsafe_allow_html=True)
            if poin_dapat > 0:
                st.info(f"⭐ Anda akan mendapat **{poin_dapat} poin** dari pesanan ini!")
            st.markdown("")
            pesan = st.button("✅ Konfirmasi Pesanan", use_container_width=True, type="primary")

    if pesan:
        if not nama or not hp:
            st.error("❌ Nama dan nomor HP wajib diisi!")
        elif kg < 0.5:
            st.error("❌ Minimal berat 0.5 kg!")
        else:
            # Cari atau buat customer baru
            cust = next((c for c in st.session_state.customers if c["hp"] == hp), None)
            if not cust:
                new_id = max(c["id"] for c in st.session_state.customers) + 1
                cust = {"id": new_id, "nama": nama, "hp": hp, "email": "", "bergabung": str(date.today()), "poin": 0, "tier": "Bronze"}
                st.session_state.customers.append(cust)

            # Buat transaksi
            tx = {
                "id": next_tx_id(), "customer_id": cust["id"], "tanggal": str(date.today()),
                "kg": kg, "layanan": layanan_pilihan, "harga": total, "status": "Menunggu",
                "poin": poin_dapat, "deterjen": "Attack", "mesin": "Mesin LG 9kg", "catatan": catatan
            }
            st.session_state.transaksi.append(tx)
            update_customer_points(cust["id"], poin_dapat)

            st.balloons()
            st.success(f"🎉 Pesanan berhasil! No. Order: **#{tx['id']}**")
            st.markdown(f"""
            <div class="success-card">
                <b>👕 {layanan_pilihan}</b> · {kg} kg<br>
                💰 Total: <b>{format_rp(total)}</b><br>
                ⭐ Poin didapat: <b>+{poin_dapat} poin</b><br>
                🕐 Status: <b>Menunggu</b>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: RIWAYAT TRANSAKSI
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Riwayat Transaksi":
    st.markdown("## 📋 Riwayat Transaksi")

    col1, col2, col3 = st.columns([2, 1.2, 1])
    with col1:
        cari = st.text_input("🔍 Cari nama / nomor HP", placeholder="Ketik untuk mencari...")
    with col2:
        filter_status = st.selectbox("Filter Status", ["Semua", "Menunggu", "Diproses", "Selesai"])
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)

    # Build display data
    rows = []
    for tx in sorted(st.session_state.transaksi, key=lambda x: x["id"], reverse=True):
        cust = find_customer(tx["customer_id"])
        if not cust:
            continue
        match_cari = not cari or cari.lower() in cust["nama"].lower() or cari in cust["hp"]
        match_status = filter_status == "Semua" or tx["status"] == filter_status
        if match_cari and match_status:
            rows.append({
                "No. Order": f"#{tx['id']}",
                "Pelanggan": cust["nama"],
                "HP": cust["hp"],
                "Tanggal": tx["tanggal"],
                "Layanan": tx["layanan"],
                "Berat (kg)": tx["kg"],
                "Deterjen": tx["deterjen"],
                "Mesin": tx["mesin"],
                "Total": format_rp(tx["harga"]),
                "Poin": f"+{tx['poin']} ⭐",
                "Status": tx["status"],
            })

    if rows:
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True, hide_index=True,
            column_config={
                "Status": st.column_config.SelectboxColumn(options=["Menunggu", "Diproses", "Selesai", "Dibatalkan"]),
            }
        )
    else:
        st.info("Tidak ada data transaksi yang sesuai.")

    st.markdown("---")
    st.markdown("### 📊 Ringkasan")
    c1, c2, c3 = st.columns(3)
    all_tx = st.session_state.transaksi
    total_omset = sum(t["harga"] for t in all_tx)
    total_kg    = sum(t["kg"]    for t in all_tx)
    avg_tx      = total_omset // len(all_tx) if all_tx else 0
    with c1:
        st.metric("💰 Total Pendapatan", format_rp(total_omset))
    with c2:
        st.metric("⚖️ Total Cucian", f"{total_kg:.1f} kg")
    with c3:
        st.metric("📊 Rata-rata/Transaksi", format_rp(avg_tx))

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: MEMBERSHIP
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Membership":
    st.markdown("## ⭐ Program Membership")
    st.markdown("Kumpulkan poin dari setiap transaksi dan nikmati berbagai hadiah menarik.")

    # Kartu member
    if st.session_state.logged_in:
        u = st.session_state.logged_in
        tier_name, tier_color, tier_icon = get_tier(u["poin"])
        if tier_name == "Bronze":
            sisa_info = f"{200 - u['poin']} poin lagi ke Silver"
        elif tier_name == "Silver":
            sisa_info = f"{500 - u['poin']} poin lagi ke Gold"
        else:
            sisa_info = "Anda sudah di tier tertinggi! 🏆"

        st.markdown(f"""
        <div class="member-card-big">
            <div style="font-size:0.75rem;letter-spacing:2px;opacity:0.7;margin-bottom:8px">CLEANWAVE MEMBER CARD</div>
            <div style="font-size:1.6rem;font-weight:900">{u['nama']}</div>
            <div style="opacity:0.8;margin-bottom:16px">{u['hp']}</div>
            <div style="font-size:3rem;font-weight:900;line-height:1">{u['poin']}</div>
            <div style="opacity:0.8;margin-bottom:8px">Poin</div>
            <div style="display:flex;align-items:center;justify-content:space-between">
                <span style="font-size:0.8rem;opacity:0.7">{sisa_info}</span>
                <span style="background:rgba(255,255,255,0.3);padding:4px 14px;border-radius:99px;font-weight:800">{tier_icon} {tier_name}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("🔒 Login terlebih dahulu untuk melihat poin dan menukar hadiah.")
        if st.button("🔑 Login Sekarang"):
            st.session_state.page = "Masuk / Daftar"
            st.rerun()

    # Tier info
    st.markdown("### 🏅 Level Keanggotaan")
    tc1, tc2, tc3 = st.columns(3)
    tier_data = [
        ("Bronze 🥉", "0–199 poin",   "1 poin per Rp 1.000",                  "#FEF9C3"),
        ("Silver 🥈", "200–499 poin", "1 poin + prioritas antrian",            "#F3F4F6"),
        ("Gold 🥇",   "500+ poin",    "1 poin + prioritas + diskon 5%",        "#FEF3C7"),
    ]
    for col, (tnama, trange, tperks, tbg) in zip([tc1, tc2, tc3], tier_data):
        with col:
            st.markdown(f"""
            <div class="tier-card" style="background:{tbg}">
                <div class="tier-name">{tnama}</div>
                <div class="tier-range">{trange}</div>
                <div class="tier-perks">{tperks}</div>
            </div>
            """, unsafe_allow_html=True)

    # Hadiah
    st.markdown("### 🎁 Tukar Poin")
    h_cols = st.columns(2)
    for i, h in enumerate(HADIAH):
        with h_cols[i % 2]:
            user_poin = st.session_state.logged_in["poin"] if st.session_state.logged_in else 0
            bisa = user_poin >= h["poin"]
            st.markdown(f"""
            <div class="reward-card {'reward-active' if bisa else ''}">
                <div style="font-size:2rem;margin-bottom:6px">{h['icon']}</div>
                <div class="reward-name">{h['nama']}</div>
                <div class="reward-desc">{h['deskripsi']}</div>
                <div class="reward-cost">{h['poin']} ⭐</div>
            </div>
            """, unsafe_allow_html=True)
            if bisa and st.session_state.logged_in:
                if st.button(f"Tukar: {h['nama']}", key=f"redeem_{i}", use_container_width=True):
                    update_customer_points(st.session_state.logged_in["id"], -h["poin"])
                    st.success(f"🎉 Berhasil menukar poin: **{h['nama']}**!")
                    st.rerun()
            else:
                st.button("Poin tidak cukup", key=f"redeem_disabled_{i}", disabled=True, use_container_width=True)

    # Tabel semua member
    st.markdown("---")
    st.markdown("### 👥 Daftar Semua Member")
    member_rows = []
    for c in sorted(st.session_state.customers, key=lambda x: x["poin"], reverse=True):
        tier_name, _, tier_icon = get_tier(c["poin"])
        member_rows.append({
            "Nama": c["nama"],
            "No. HP": c["hp"],
            "Bergabung": c["bergabung"],
            "Tier": f"{tier_icon} {tier_name}",
            "Poin": c["poin"],
        })
    st.dataframe(pd.DataFrame(member_rows), use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: ALAT & BAHAN
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Alat & Bahan":
    st.markdown("## 🔧 Alat & Bahan")
    st.markdown("Informasi peralatan dan bahan yang kami gunakan untuk layanan terbaik.")

    st.markdown("### 🏭 Peralatan Laundry")
    pc1, pc2 = st.columns(2)
    for i, eq in enumerate(PERALATAN):
        with (pc1 if i % 2 == 0 else pc2):
            st.markdown(f"""
            <div class="equip-card">
                <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px">
                    <span style="font-size:2rem">{eq['icon']}</span>
                    <div>
                        <div style="font-weight:800;font-size:1rem">{eq['nama']}</div>
                        <div style="font-size:0.8rem;color:#64748B">{eq['kategori']} · {eq['brand']}</div>
                    </div>
                </div>
                <div style="font-size:0.875rem;color:#64748B;margin-bottom:8px">{eq['deskripsi']}</div>
                {'<span class="badge-blue">⚖️ Kapasitas: ' + eq["kapasitas"] + '</span>' if eq["kapasitas"] != "-" else ""}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### 🧴 Bahan & Produk Kebersihan")
    bc1, bc2, bc3 = st.columns(3)
    for i, b in enumerate(BAHAN):
        with [bc1, bc2, bc3][i % 3]:
            st.markdown(f"""
            <div class="material-card">
                <div style="font-size:2rem;margin-bottom:6px">{b['icon']}</div>
                <div style="font-weight:800;font-size:1rem">{b['nama']}</div>
                <span class="badge-blue">{b['tipe']}</span>
                <div style="font-size:0.8rem;color:#64748B;margin-top:8px"><b>Kegunaan:</b> {b['kegunaan']}</div>
                <div style="font-size:0.75rem;color:#94A3B8;margin-top:4px">✅ {b['cocok']}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🌿 Komitmen Kami")
    k1, k2 = st.columns(2)
    komitmen = [
        "✅ Deterjen ramah lingkungan & biodegradable",
        "✅ Air bersih hasil filtrasi RO",
        "✅ Tidak menggunakan bahan berbahaya / keras",
        "✅ Peralatan dicuci & dirawat secara berkala",
    ]
    for i, k in enumerate(komitmen):
        with (k1 if i % 2 == 0 else k2):
            st.markdown(f'<div class="komitmen-item">{k}</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: MASUK / DAFTAR
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Masuk / Daftar":
    st.markdown("## 🔑 Masuk / Daftar")
    col_mid, _ = st.columns([1.2, 1])
    with col_mid:
        tab_login, tab_daftar = st.tabs(["🔑 Masuk", "📝 Daftar Baru"])

        with tab_login:
            st.markdown("Masuk menggunakan nomor HP terdaftar.")
            hp_login = st.text_input("Nomor HP", placeholder="08xxxxxxxxxx", key="hp_login")
            if st.button("Masuk", type="primary", use_container_width=True):
                cust = next((c for c in st.session_state.customers if c["hp"] == hp_login), None)
                if cust:
                    st.session_state.logged_in = cust
                    st.success(f"✅ Selamat datang, **{cust['nama']}**!")
                    st.session_state.page = "Beranda"
                    st.rerun()
                else:
                    st.error("❌ Nomor HP tidak ditemukan. Coba daftar dulu.")
            st.caption("**Demo:** gunakan `081234567890`, `082345678901`, atau `083456789012`")

        with tab_daftar:
            st.markdown("Daftar sebagai member baru untuk mendapatkan poin.")
            nama_reg = st.text_input("Nama Lengkap", key="nama_reg")
            hp_reg   = st.text_input("Nomor HP", placeholder="08xxxxxxxxxx", key="hp_reg")
            email_reg= st.text_input("Email (opsional)", placeholder="email@contoh.com", key="email_reg")
            if st.button("Daftar Sekarang", type="primary", use_container_width=True):
                if not nama_reg or not hp_reg:
                    st.error("❌ Nama dan HP wajib diisi!")
                elif any(c["hp"] == hp_reg for c in st.session_state.customers):
                    st.error("❌ Nomor HP sudah terdaftar!")
                else:
                    new_id = max(c["id"] for c in st.session_state.customers) + 1
                    new_cust = {"id": new_id, "nama": nama_reg, "hp": hp_reg, "email": email_reg,
                                "bergabung": str(date.today()), "poin": 0, "tier": "Bronze"}
                    st.session_state.customers.append(new_cust)
                    st.session_state.logged_in = new_cust
                    st.success(f"🎉 Berhasil daftar! Selamat datang, **{nama_reg}**!")
                    st.session_state.page = "Beranda"
                    st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: PROFIL
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Profil Saya":
    if not st.session_state.logged_in:
        st.warning("Anda belum login.")
        st.stop()

    u = st.session_state.logged_in
    tier_name, tier_color, tier_icon = get_tier(u["poin"])

    st.markdown(f"## 👤 Profil: {u['nama']}")
    col_info, col_tx = st.columns([1, 1.8])

    with col_info:
        with st.container(border=True):
            st.markdown(f"**Nama:** {u['nama']}")
            st.markdown(f"**No. HP:** {u['hp']}")
            st.markdown(f"**Email:** {u['email'] or '-'}")
            st.markdown(f"**Bergabung:** {u['bergabung']}")
            st.markdown(f"**Tier:** {tier_icon} {tier_name}")
            st.metric("⭐ Poin Saya", u["poin"])

    with col_tx:
        st.markdown("#### 📋 Riwayat Transaksi Saya")
        my_tx = [t for t in st.session_state.transaksi if t["customer_id"] == u["id"]]
        if my_tx:
            rows = [{"Tanggal": t["tanggal"], "Layanan": t["layanan"],
                     "Berat": f"{t['kg']} kg", "Total": format_rp(t["harga"]),
                     "Poin": f"+{t['poin']}⭐", "Status": t["status"]} for t in sorted(my_tx, key=lambda x: x["id"], reverse=True)]
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        else:
            st.info("Belum ada transaksi.")
