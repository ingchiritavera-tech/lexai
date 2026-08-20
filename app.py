import streamlit as st

# Configurare interfață mobilă profesională
st.set_page_config(page_title="LexAI Pro", page_icon="⚖️", layout="centered")

# Stiluri personalizate — atenție: poate fi fragil față de versiuni Streamlit
st.markdown("""
    <style>
    /* Fundal și text principal */
    .stApp { background-color: #121212; color: #FFFFFF; }

    /* Butoane mari și consistente */
    div.stButton > button {
        font-size: 18px !important;
        font-weight: 700 !important;
        height: 55px !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        border: none !important;
        margin-bottom: 12px !important;
        width: 100% !important;
    }

    /* Selectorii pentru butoane specifice pot fi nesiguri; nth-of-type folosit ca fallback */
    /* Primul buton */
    div.stButton:nth-of-type(1) > button { background-color: #FF5722 !important; }
    /* Al doilea buton */
    div.stButton:nth-of-type(2) > button { background-color: #D32F2F !important; }
    /* Al treilea buton */
    div.stButton:nth-of-type(3) > button { background-color: #1976D2 !important; }

    .box-expertiza {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FFCC00;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚖️ LexAI - Management Legal")
st.subheader("Modul: Penal & Administrativ Local")

# Avertisment de confidențialitate / limitare
st.info("Atenție: Nu trimiteți date personale sensibile. Informațiile generate sunt șabloane și nu constituie consultanță juridică.")

# Caseta de introducere text
document_text = st.text_area(
    "📋 Lipiți actul suspect sau declarația:",
    height=150,
    placeholder="Introduceți textul dispoziției sau al dosarului penal..."
)

# Inițializare sigură st.session_state
if "doc_type" not in st.session_state:
    st.session_state.doc_type = None

# Callback-uri pentru butoane
def set_doc_type(t):
    st.session_state.doc_type = t

st.markdown("### 🎛️ PANOU DE CONTROL INTERACTIV (Apasă pentru document):")

# Folosim un container pentru a forța ordine verticală pe mobil
with st.container():
    # Butoane — folosim key-uri și on_click pentru stabilitate
    st.button("🛑 1. GENEREAZĂ SESIZARE PREFECT / AFIR", key="sesizare_btn", on_click=set_doc_type, args=("sesizare",))
    st.button("⚖️ 2. GENEREAZĂ PLÂNGERE PENALĂ", key="plangere_btn", on_click=set_doc_type, args=("plangere",))
    st.button("✉️ 3. GENEREAZĂ ADRESĂ DE REVOCARE", key="revocare_btn", on_click=set_doc_type, args=("revocare",))

# Dacă s-a selectat tipul de document, afișăm textul corespunzător
if st.session_state.doc_type:
    st.write("---")
    if st.session_state.doc_type == "sesizare":
        st.success("✅ Text sesizare pregătit pentru copiere:")
        st.code(
            "Către: Prefectul Județului...\n\n"
            "Prin prezenta sesizez nelegalitatea actului administrativ...\n\n"
            "— (adaugați datele relevante și probele)"
        )
    elif st.session_state.doc_type == "plangere":
        st.success("✅ Text plângere penală (Art. 289 C.proc.pen.) pregătit pentru copiere:")
        st.code(
            "Către: Parchetul de pe lângă Judecătoria...\n\n"
            "Formulez plângere penală împotriva numitului...\n\n"
            "— (adaugați datele, fapta, probele și martorii)"
        )
    elif st.session_state.doc_type == "revocare":
        st.success("✅ Text adresă de revocare pregătit pentru copiere:")
        st.code(
            "Către: Primăria...\n\n"
            "Solicit revocarea în tot a deciziei nelegale conform Legii 554/2004...\n\n"
            "— (adaugați motivarea și temeiurile juridice)"
        )
