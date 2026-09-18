import streamlit as st
import time

# Pengaturan Konfigurasi Halaman Browser
st.set_page_config(page_title="Hadiah Untuk Sayang", page_icon="💗", layout="centered")

# Menggunakan CSS Custom agar tampilannya bernuansa Pink manis di HP
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1, h2, h3, p { color: #5C3A4D !important; text-align: center; }
    .stButton>button {
        background-color: #FF69B4 !important; color: white !important;
        border-radius: 20px; padding: 10px 25px; font-weight: bold;
        border: none; display: block; margin: 0 auto;
    }
    .stButton>button:hover { background-color: #D63384 !important; }
    .heart-bg { font-size: 24px; text-align: center; color: #FF69B4; animation: pulse 1s infinite; }
    </style>
""", unsafe_allow_index=True)

# Inisialisasi state halaman agar bisa berpindah saat tombol diklik
if 'page' not in st.session_state:
    st.session_state.page = 'pembuka'

# --- HALAMAN PEMBUKA ---
if st.session_state.page == 'pembuka':
    st.markdown("<h1 style='color: #D63384;'>💗 UNTUK KAMU 💗</h1>", unsafe_allow_index=True)
    st.write("Ada sedikit sesuatu yang ingin mas lidooo kasii buat kamuu...")
    st.write("")
    st.markdown("""
    Hai Sayangkuu issahhh ❤️  
    Aku tahuu kok kamu lagii enggaa enak badann.  
    Jadi aku bikinn sesuatu kecil kecilan untuk kmuu.  
    
    Memang enggak bisa menggantikan pelukan langsung,  
    tapi semoga sedikit bisa bikin kmuuu tersenyum.
    """)
    st.write("")
    if st.button("🎁 BUKA HADIAH"):
        st.session_state.page = 'hadiah1'
        st.rerun()

# --- HADIAH 1 ---
elif st.session_state.page == 'hadiah1':
    st.markdown("<h2 style='color: #D63384;'>💌 HADIAH PERTAMA</h2>", unsafe_allow_index=True)
    st.markdown("""
    Hai Sayangkuu issahhh ❤️  
    Aku tahu akhir-akhir ini perut kmuu lagii enggaa nyamann.  
    Mungkin badanmu terasa capek dan mood juga naik turun.  
    
    Jadi untuk sekarang, jangan terlalu memaksakan diri ya.  
    Istirahat yang cukupp yaa, minum air yang cukup jugaa,  
    dan lakukan hal-hal yang bikin kmuuu nyaman.  
    
    mas lidoo mungkin tidak bisa menghilangkan rasa sakitnya,  
    tapi mas lidoo selaluu bisa temenin kmuuu. ❤️
    """)
    if st.button("🫂 BUKA HADIAH BERIKUTNYA"):
        st.session_state.page = 'hadiah2'
        st.rerun()

# --- HADIAH 2 ---
elif st.session_state.page == 'hadiah2':
    st.markdown("<h2 style='color: #D63384;'>🫂 HADIAH KEDUA</h2>", unsafe_allow_index=True)
    st.markdown("<h1 style='font-size: 80px;'>🫂</h1>", unsafe_allow_index=True)
    st.markdown("""
    **INI PELUKAN DARI mas lidoo ❤️**  
    Kalau mas lidoo ada di samping aisyahh sekarang,  
    mungkin mas lidoo sudah peluk eratt eratt, terus pugpug kepala aisyahhh.  
    
    Jadi untukk sementaraaa,  
    anggap emoji ini sebagai pelukan dari mas lidoo yaa.
    """)
    if st.button("🍫 LANJUT KE HADIAH BERIKUTNYA"):
        st.session_state.page = 'hadiah3'
        st.rerun()

# --- HADIAH 3 ---
elif st.session_state.page == 'hadiah3':
    st.markdown("<h2 style='color: #D63384;'>🍫 HADIAH KETIGA</h2>", unsafe_allow_index=True)
    st.markdown("<h1 style='font-size: 60px;'>🍫🍫🍫</h1>", unsafe_allow_index=True)
    st.markdown("""
    **COKELAT UNTUKMU ❤️**  
    Ini memangg baruu cokelatt virtuall...  
    tapi yangg aslinyaa bisaa menyusulll 😌  
    
    Kalau mas lidoo lagii cairr,  
    sudah pasti uddaa mas lidoo bawakann cokelatt benerann.
    """)
    if st.button("🌷 LANJUT"):
        st.session_state.page = 'hadiah4'
        st.rerun()

# --- HADIAH 4 ---
elif st.session_state.page == 'hadiah4':
    st.markdown("<h2 style='color: #D63384;'>🌷 HADIAH KEEMPAT</h2>", unsafe_allow_index=True)
    st.markdown("<h1 style='font-size: 80px;'>🌷</h1>", unsafe_allow_index=True)
    st.markdown("""
    **SATU BUNGA UNTUKMU 🌷**  
    Bunganya memang cuma digitalll,  
    tapi orangg yang kasiii inii sayanggg sekalii sama kamuuu loo. ❤️  
    
    Semoga harii kamuu jadii sedikit lebihh indahhh yaa 🫶🫶path.
    """)
    if st.button("😂 LANJUT KE HADIAH TERAKHIR"):
        st.session_state.page = 'hadiah5'
        st.rerun()

# --- HADIAH 5 ---
elif st.session_state.page == 'hadiah5':
    st.markdown("<h2 style='color: #D63384;'>😂 HADIAH TERAKHIR</h2>", unsafe_allow_index=True)
    st.markdown("<h1 style='font-size: 60px;'>😤</h1>", unsafe_allow_index=True)
    st.markdown("""
    **HARAPAN AKUUUU:**  
    **KAMU BISAA SENYUM SEKARANGGG! 😤❤️**  
    Kenapaaa???  
    Karena kamuuu lebihhh cuannntikkk kalau senyummm.  
    
    Walaupunn hari inii terasa beratt,  
    kamu enggaa harusss melewati semuanyaa sendiriannn 🥹.
    """)
    if st.button("😁 AKU SENYUM"):
        st.session_state.page = 'ending'
        st.rerun()

# --- ENDING ---
elif st.session_state.page == 'ending':
    st.balloons() # Efek balon meluncur di layar HP saat sukses selesai
    st.markdown("<h2 style='color: #D63384;'>❤️ HADIAH TERAKHIR ❤️</h2>", unsafe_allow_index=True)
    st.markdown("<h1 style='font-size: 60px;'>❤️</h1>", unsafe_allow_index=True)
    st.markdown("""
    Terima kasih sudah membuka semua hadiahnyaaa yaaa, Sayangkuu issahhh. ❤️  
    Aku harap kamu cepet ngerasa baikannn.  
    Jangan lupa istirahattt dan jangann terlalu memaksakan dirii yaa.  
    
    Kalau hari ini kamu merasa tidak baik-baik sajaa,  
    tidak apaa-apaaa. Istirahattt duluuu.  
    Semoga hadiah kecil dari mas lidoo ini bisa bikin aisyahh tersenyum meski cuma sedikit.  
    
    **❤️ AKUUU SAYANGGG KAMUUU AISYAAHHHHHH ❤️**
    """)
    if st.button("🔄 BUKA LAGI DARI AWAL"):
        st.session_state.page = 'pembuka'
        st.rerun()
