import streamlit as st
from datetime import datetime
import pandas as pd
import base64

# Configuración inicial de la página
st.set_page_config(
    page_title="OmniJourney - Chatbots con Propósito, promoción con visibilidad",
    layout="wide"
)

# Function to encode image as base64 to set as background
def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Encode the background image
img_base64 = get_base64_of_bin_file('background.jpg')

    # Set the background image using the encoded base64 string
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url('data:image/jpeg;base64,{img_base64}') no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ SELECTOR DE IDIOMA ------------------
col1, col2 = st.columns([1, 19])
selected_language = st.session_state.get("language", "es")  # Por defecto español
with col1:
    if st.button("![ES](https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png)", key="spanish_button"):
        selected_language = "es"
with col2:
    if st.button("![EN](https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg)", key="english_button"):
        selected_language = "en"

# Guardar idioma seleccionado
if "language" not in st.session_state:
    st.session_state.language = selected_language
elif st.session_state.language != selected_language:
    st.session_state.language = selected_language
    st.rerun()

# ------------------ DICCIONARIO DE TRADUCCIÓN ------------------
translations = {
    "es": {
        "title": "🤖 OmniJourney",
        "subtitle": "Chatbots con Propósito para transformar tu marca y generar visibilidad global.",
        "what_is": "🌟 ¿Qué es OmniJourney?",
        "description": """
OmniJourney es una plataforma innovadora de visibilidad digital que permite a profesionales, empresas y marcas personales crear y promocionar chatbots personalizados sin necesidad de conocimientos técnicos, para brindar atención 24/7, captar leads, resolver dudas y fortalecer su posicionamiento online.

A diferencia de otras soluciones genéricas, OmniJourney combina desarrollo personalizado de asistentes virtuales + exposición directa al público objetivo, conectando oferta con demanda en un entorno digital inteligente.
        """,
        "benefits_title": "🚀 Beneficios de usar nuestros chatbots",
        "benefits": [
            "Automatiza la atención al cliente 24/7",
            "Convierte visitantes en clientes potenciales",
            "Responde preguntas frecuentes al instante",
            "Personaliza la experiencia de cada usuario",
            "Refuerza la identidad y propósito de tu marca",
            "Reduce costos de atención al cliente",
            "Mejora la imagen profesional de tu empresa"
        ],
        "platform_title": "🧠 Beneficios de la plataforma OmniJourney",
        "platform_benefits": [
            "Sin necesidad de saber programar",
            "Diseño y desarrollo de tu asistente incluido",
            "Publicación en nuestro portal con visibilidad directa",
            "Difusión en redes y campañas promocionales",
            "Entrenamiento con tus documentos y servicios",
            "Soporte humano + IA",
            "Ideal para profesionales, marcas personales y empresas"
        ],
        "footer": "© 2024 OmniJourney. Impulsado por IA.",
        "contact_us": "📩 Contáctanos"
    },
    "en": {
        "title": "🤖 OmniJourney",
        "subtitle": "Purpose-Driven Chatbots to transform your brand and generate global visibility.",
        "what_is": "🌟 What is OmniJourney?",
        "description": """
OmniJourney is an innovative digital visibility platform that allows professionals, companies, and personal brands to create and promote personalized chatbots without technical knowledge, offering 24/7 customer service, lead capture, Q&A, and brand strengthening.

Unlike generic solutions, OmniJourney combines custom virtual assistant development + direct exposure to your target audience, connecting supply and demand in a smart digital environment.
        """,
        "benefits_title": "🚀 Benefits of using our chatbots",
        "benefits": [
            "Automate 24/7 customer support",
            "Turn visitors into potential clients",
            "Instant answers to frequently asked questions",
            "Customize each user experience",
            "Reinforce your brand's identity and purpose",
            "Reduce customer support costs",
            "Enhance your company's professional image"
        ],
        "platform_title": "🧠 Benefits of the OmniJourney platform",
        "platform_benefits": [
            "No programming knowledge required",
            "Design and development of your assistant included",
            "Publication on our portal with direct visibility",
            "Promotion through social media campaigns",
            "Training with your documents and services",
            "Human + AI support",
            "Perfect for professionals, personal brands, and companies"
        ],
        "footer": "© 2024 OmniJourney. Powered by AI.",
        "contact_us": "📩 Contact Us"
    }
}

# ------------------ FUNCIÓN DE TRADUCCIÓN ------------------
def t(key):
    return translations[st.session_state.language].get(key, key)

# ------------------ ESTILO PERSONALIZADO ------------------
st.markdown("""
    <style>
    .main {
        background-color: #04B404;
    }
    .title {
        font-size: 3em;
        font-weight: bold;
        color: #4b2aad;
    }
    .subtitle {
        font-size: 1.5em;
        color: #555;
        margin-bottom: 1em;
    }
    .section {
        margin-top: 2em;
        padding: 1.5em;
        background-color: #ffffffcc;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ CONTENIDO ------------------
st.markdown(f'<div class="title">{t("title")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="subtitle">{t("subtitle")}</div>', unsafe_allow_html=True)
st.divider()

# st.markdown('<div class="section">', unsafe_allow_html=True)
st.subheader(t("what_is"))
st.write(t("description"))
st.markdown('</div>', unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns([1, 1])
with col1:
    with st.expander(t("benefits_title"), expanded=False):
        
        for line in t("benefits"):
            st.markdown(f"- {line}")
        st.markdown('</div>', unsafe_allow_html=True)
   

with col2:
    with st.expander(t("platform_title"), expanded= False):
        for line in t("platform_benefits"):
            st.markdown(f"- {line}")
        st.markdown('</div>', unsafe_allow_html=True)


st.divider()

# ------------------ BOTÓN DE DESCARGA DE PDF ------------------
download_message = {
    "es": "¿Quieres saber más sobre nosotros?",
    "en": "Want to know more about us?"
}
with st.container():
        # st.markdown('<div class="section">', unsafe_allow_html=True)
        st.write(download_message[st.session_state.language])
        with open("OmniJourney_PDF.pdf", "rb") as pdf_file:
            pdf_data = pdf_file.read()
        col1, col2 = st.columns([1, 3])
        with col1:    
            st.download_button(
                label=t("Descarga información en español"),
                data=pdf_data,
                file_name="OmniJourney_PDF.pdf",
                mime="application/pdf"
    )
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            with open("OmniJourney_PDF_EN.pdf", "rb") as pdf_file:
                pdf_data_en = pdf_file.read()
            st.download_button(
            label=t("Download information in English"),
            data=pdf_data_en,
            file_name="OmniJourney_PDF_EN.pdf",
            mime="application/pdf"
    )
            st.markdown('</div>', unsafe_allow_html=True)

# ------------------- FORMULARIO de contacto y contacto via  whatssap -------------------
st.subheader(t("contact_us"))

WhatsApp_message = {
        "es": "¿Quieres hablar con nosotros por WhatsApp?, Asi es mas directo!",
        "en": "Do you want to talk to us on WhatsApp? Is more direct!"
    }
st.write(WhatsApp_message[st.session_state.language])
st.markdown("[WhatsApp](https://wa.me/5930993513082?text=Hola%20OmniJourney,%20quiero%20más%20información)", unsafe_allow_html=True)



# ------------------ PIE DE PÁGINA ------------------
st.markdown("---")
st.caption(t("footer"))
