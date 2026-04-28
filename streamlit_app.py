import streamlit as st
from datetime import date
import pandas as pd
import os

# ─── PAGE CONFIG ─────────────────────────────────────────────
st.set_page_config(
    page_title="CleanWave Laundry",
    page_icon="🌊",
    layout="wide",
)

# ─── LOAD CSS (FIXED) ────────────────────────────────────────
def load_css():
    css_path = os.path.join(os.getcwd(), "style.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ style.css tidak ditemukan, menggunakan tampilan default.")

load_css()

# ─── DATA DEFAULT ────────────────────────────────────────────
DEFAULT_CUSTOMERS = [
    {"id": 1, "nama": "Budi Santoso", "hp": "081234567890", "email": "", "bergabung": "2024-01-10", "poin": 320, "tier": "Silver"},
    {"id": 2, "nama": "Siti Rahayu", "hp": "082345678901", "email": "", "bergabung": "2024-02-15", "poin": 750, "tier": "Gold"},
]

DEFAULT_TRANSAKSI = []

LAYANAN = {
    "Cuci & Setrika": 10000,
    "Cuci Kering": 8000,
    "Setrika Saja": 7000,
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

# ─── SIDEBAR (FIXED SPLIT) ───────────────────────────────────
with st.sidebar:
    st.title("🌊 CleanWave Laundry")

    menu = ["🏠 Beranda", "📦 Pesan Laundry", "📋 Riwayat", "🔑 Login"]
    selected = st.radio("Menu", menu)

    if " " in selected:
        page = selected.split(" ", 1)[1]
    else:
        page = selected

    st.session_state.page = page

# ─── BERANDA ────────────────────────────────────────────────
if page == "Beranda":
    st.title("CleanWave Laundry 🌊")
    st.write("Selamat datang di sistem laundry digital.")

# ─── PESAN ─────────────────────────────────────────────────
elif page == "Pesan Laundry":
    st.header("Pesan Laundry")

    nama = st.text_input("Nama")
    hp = st.text_input("No HP")

    layanan = st.selectbox("Layanan", list(LAYANAN.keys()))
    kg = st.number_input("Berat (kg)", min_value=0.5, value=1.0)

    total = kg * LAYANAN[layanan]

    st.write(f"Total: {format_rp(total)}")

    if st.button("Pesan"):
        if not nama or not hp:
            st.error("Nama & HP wajib!")
        elif not hp.isdigit():
            st.error("HP harus angka!")
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
                "status": "Menunggu"
            }

            st.session_state.transaksi.append(tx)

            st.success(f"Pesanan berhasil! ID: {tx['id']}")

# ─── RIWAYAT ────────────────────────────────────────────────
elif page == "Riwayat":
    st.header("Riwayat Transaksi")

    if st.session_state.transaksi:
        df = pd.DataFrame(st.session_state.transaksi)
        st.dataframe(df)
    else:
        st.info("Belum ada transaksi")

# ─── LOGIN ──────────────────────────────────────────────────
elif page == "Login":
    st.header("Login")

    hp = st.text_input("No HP")

    if st.button("Masuk"):
        cust = next((c for c in st.session_state.customers if c["hp"] == hp), None)
        if cust:
            st.session_state.logged_in = cust
            st.success(f"Selamat datang {cust['nama']}")
        else:
            st.error("HP tidak ditemukan")
