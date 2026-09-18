import streamlit as st
import base64

# =========================================================================
# 🎵 NAMA FILE MUSIK KAMU (Harus sama persis dengan yang di-upload di GitHub)
# =========================================================================
NAMA_FILE_MUSIK = "klbmusik.mp3" 

# Pengaturan Konfigurasi Halaman Browser
st.set_page_config(page_title="Hadiah Untuk Sayang", page_icon="💗", layout="centered")

# Menggunakan CSS Custom untuk tampilan tema Pink manis dan Animasi Amplop Surat
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
    
    /* --- Gaya Visual Amplop Surat --- */
    .envelope-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 30px auto;
        perspective: 1000px;
    }
    .envelope {
        position: relative;
        width: 180px;
        height: 120px;
        background: #F48FB1;
        border-radius: 0 0 10px 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    /* Bagian Lipatan Segitiga Atas Amplop */
    .envelope::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 0;
        height: 0;
        border-left: 90px solid transparent;
        border-right: 90px solid transparent;
        border-top: 65px solid #F06292;
        transform-origin: top;
        transition: transform 0.4s ease;
        z-index: 2;
    }
    /* Bagian Dalam Jalur Surat keluar */
    .letter {
        position: absolute;
        top: 10px;
        left: 15px;
        width: 150px;
        height: 90px;
        background: #FFFFFF;
        border-radius: 5px;
        z-index: 1;
        transition: transform 0.4s ease;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
    }
    /* Animasi saat tombol ditekan (efek membuka) */
    .open::before {
        transform: rotateX(180px);
        z-index: 0;
    }
    .open .letter {
        transform: translateY(-40px);
    }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk memutar musik latar secara tersembunyi
def mainkan_musik_latar(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay loop style="display:none;">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        pass

# Inisialisasi state halaman & musik agar bisa terpantau
if 'page' not in st.session_state:
    st.session_state.page = 'pembuka'
if 'musik_dinyalakan' not in st.session_state:
    st.session_state.musik_dinyalakan = False

# 🎵 KUNCI PERBAIKAN: Jika musik sudah dipicu sekali, ia akan terus dimuat di halaman mana pun termasuk saat reset ke awal
if st.session_state.musik_dinyalakan:
    mainkan_musik_latar(NAMA_FILE_MUSIK)

# --- HALAMAN PEMBUKA ---
if st.session_state.page == 'pembuka':
    st.markdown("<h1 style='color: #D63384;'>💗 UNTUK KAMU 💗</h1>", unsafe_allow_html=True)
    st.write("Ada sedikit sesuatu yang ingin mas lidooo kasii buat kamuu...")
    st.write("")
    
    # Menampilkan Visual Amplop Tertutup
    st.markdown("""
        <div class="envelope-container">
            <div class="envelope">
                <div class="letter">❤️</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Hai Sayangkuu issahhh ❤️  
    Aku tahuu kok kamu lagii enggaa enak badann.  
    Jadi aku bikinn sesuatu kecil kecilan untuk kmuu.  
    
    Memang enggak bisa menggantikan pelukan langsung,  
    tapi semoga sedikit bisa bikin kmuuu tersenyum.
    """)
    st.write("")
    if st.button("🎁 BUKA AMPLOP"):
        st.session_state.musik_dinyalakan = True # Memicu musik menyala permanen
        st.session_state.page = 'hadiah1'
        st.rerun()

# --- HADIAH 1 ---
elif st.session_state.page == 'hadiah1':
    st.markdown("<h2 style='color: #D63384;'>💌 HADIAH PERTAMA</h2>", unsafe_allow_html=True)
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
    st.markdown("<h2 style='color: #D63384;'>🫂 HADIAH KEDUA</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 80px;'>🫂</h1>", unsafe_allow_html=True)
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
    st.markdown("<h2 style='color: #D63384;'>🍫 HADIAH KETIGA</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 60px;'>🍫🍫🍫</h1>", unsafe_allow_html=True)
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
    st.markdown("<h2 style='color: #D63384;'>🌷 HADIAH KEEMPAT</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 80px;'>🌷</h1>", unsafe_allow_html=True)
    st.markdown("""
    **SATU BUNGA UNTUKMU 🌷**  
    Bunganya memang cuma digitalll,  
    tapi orangg yang kasiii inii sayanggg sekalii sama kamuuu loo. ❤️  
    
    Semoga harii kamuu jadii sedikit lebihh indahhh yaa 🫶🫶.
    """)
    if st.button("😂 LANJUT KE HADIAH TERAKHIR"):
        st.session_state.page = 'hadiah5'
        st.rerun()

# --- HADIAH 5 ---
elif st.session_state.page == 'hadiah5':
    st.markdown("<h2 style='color: #D63384;'>😂 HADIAH TERAKHIR</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 60px;'>😤</h1>", unsafe_allow_html=True)
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
    st.balloons() 
    st.markdown("<h2 style='color: #D63384;'>❤️ HADIAH TERAKHIR ❤️</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 60px;'>❤️</h1>", unsafe_allow_html=True)
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
