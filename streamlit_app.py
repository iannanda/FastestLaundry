import streamlit as st
from datetime import date
import pandas as pd
import os

# ─── PAGE CONFIG ─────────────────────────────────────────────
st.set_page_config(
    page_title="CleanWave Laundry",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── LOAD CSS (FIXED) ────────────────────────────────────────
def load_css():
    css_path = os.path.join(os.getcwd(), "style.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.info("Style default digunakan (style.css tidak ditemukan)")

load_css()

# ─── DATA DEFAULT ────────────────────────────────────────────
DEFAULT_CUSTOMERS = [
    {"id": 1, "nama": "Budi Santoso", "hp": "081234567890", "email": "budi@email.com", "bergabung": "2024-01-10", "poin": 320, "tier": "Silver"},
    {"id": 2, "nama": "Siti Rahayu", "hp": "082345678901", "email": "siti@email.com", "bergabung": "2024-02-15", "poin": 750, "tier": "Gold"},
]

DEFAULT_TRANSAKSI = []

LAYANAN = {
    "Cuci & Setrika": 10000,
    "Cuci Kering": 8000,
    "Setrika Saja": 7000,
    "Express (6 jam)": 15000,
}

# ─── SESSION STATE ───────────────────────────────────────────
def init_state():
    if "customers" not in st.session_state:
        st.session_state.customers = DEFAULT_CUSTOMERS.copy()
    if "transaksi" not in st.session_state:
        st.session_state.transaksi = DEFAULT_TRANSAKSI.copy()
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = None
    if "page" not in st.session_state:
        st.session_state.page = "Beranda"

init_state()

# ─── HELPER ─────────────────────────────────────────────────
def format_rp(x):
    return f"Rp {int(x):,}".replace(",", ".")

def next_id(data):
    return max([d["id"] for d in data], default=0) + 1

def get_tier(poin):
    if poin >= 500:
        return "Gold", "🥇"
    elif poin >= 200:
        return "Silver", "🥈"
    else:
        return "Bronze", "🥉"

def find_customer(cid):
    return next((c for c in st.session_state.customers if c["id"] == cid), None)

# ─── SIDEBAR (FIXED) ─────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🌊 CleanWave Laundry")

    if st.session_state.logged_in:
        u = st.session_state.logged_in
        tier, icon = get_tier(u["poin"])
        st.success(f"{u['nama']} ({icon} {tier})")

    menu = ["🏠 Beranda", "📦 Pesan Laundry", "📋 Riwayat Transaksi", "🔑 Masuk / Daftar"]

    selected = st.radio("Menu", menu)

    # FIX SPLIT
    if " " in selected:
        page = selected.split(" ", 1)[1]
    else:
        page = selected

    st.session_state.page = page

    if st.session_state.logged_in:
        if st.button("Logout"):
            st.session_state.logged_in = None
            st.rerun()

# ─── BERANDA ────────────────────────────────────────────────
if page == "Beranda":
    st.title("CleanWave Laundry 🌊")
    st.write("Layanan laundry digital modern berbasis Streamlit.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👥 Pelanggan", len(st.session_state.customers))
    with col2:
        st.metric("📦 Transaksi", len(st.session_state.transaksi))
    with col3:
        total = sum(t["harga"] for t in st.session_state.transaksi)
        st.metric("💰 Omset", format_rp(total))

# ─── PESAN ─────────────────────────────────────────────────
elif page == "Pesan Laundry":
    st.header("Pesan Laundry")

    nama = st.text_input("Nama")
    hp = st.text_input("No HP")

    layanan = st.selectbox("Layanan", list(LAYANAN.keys()))
    kg = st.number_input("Berat (kg)", min_value=0.5, value=1.0)

    total = kg * LAYANAN[layanan]
    poin = int(total // 1000)

    st.info(f"Total: {format_rp(total)} | Poin: {poin}")

    if st.button("Pesan"):
        if not nama or not hp:
            st.error("Nama & HP wajib")
        elif not hp.isdigit():
            st.error("HP harus angka")
        else:
            cust = next((c for c in st.session_state.customers if c["hp"] == hp), None)

            if not cust:
                cust = {
                    "id": next_id(st.session_state.customers),
                    "nama": nama,
                    "hp": hp,
                    "email": "",
                    "bergabung": str(date.today()),
                    "poin": 0,
                    "tier": "Bronze"
                }
                st.session_state.customers.append(cust)

            tx = {
                "id": next_id(st.session_state.transaksi),
                "customer_id": cust["id"],
                "tanggal": str(date.today()),
                "kg": kg,
                "layanan": layanan,
                "harga": total,
                "status": "Menunggu",
                "poin": poin
            }

            st.session_state.transaksi.append(tx)

            cust["poin"] += poin

            st.success(f"Pesanan berhasil! ID: {tx['id']}")

# ─── RIWAYAT ────────────────────────────────────────────────
elif page == "Riwayat Transaksi":
    st.header("Riwayat Transaksi")

    rows = []
    for tx in st.session_state.transaksi:
        cust = find_customer(tx["customer_id"])
        rows.append({
            "ID": tx["id"],
            "Nama": cust["nama"] if cust else "-",
            "Tanggal": tx["tanggal"],
            "Layanan": tx["layanan"],
            "Total": format_rp(tx["harga"]),
            "Status": tx["status"]
        })

    if rows:
        st.dataframe(pd.DataFrame(rows), use_container_width=True)
    else:
        st.info("Belum ada transaksi")

# ─── LOGIN ──────────────────────────────────────────────────
elif page == "Masuk / Daftar":
    st.header("Login / Daftar")

    tab1, tab2 = st.tabs(["Login", "Daftar"])

    with tab1:
        hp = st.text_input("No HP")
        if st.button("Masuk"):
            cust = next((c for c in st.session_state.customers if c["hp"] == hp), None)
            if cust:
                st.session_state.logged_in = cust
                st.success(f"Selamat datang {cust['nama']}")
                st.rerun()
            else:
                st.error("Tidak ditemukan")

    with tab2:
        nama = st.text_input("Nama", key="reg_nama")
        hp = st.text_input("HP", key="reg_hp")

        if st.button("Daftar"):
            if not nama or not hp:
                st.error("Isi semua")
            else:
                cust = {
                    "id": next_id(st.session_state.customers),
                    "nama": nama,
                    "hp": hp,
                    "email": "",
                    "bergabung": str(date.today()),
                    "poin": 0,
                    "tier": "Bronze"
                }
                st.session_state.customers.append(cust)
                st.success("Berhasil daftar")
