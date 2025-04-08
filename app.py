import streamlit as st
from chatbot.chatbot import chat_with_bot
from admin_dashboard import admin_dashboard
from user_dashboard import user_dashboard
from database.database import get_all_chatbots, authenticate_user, create_chatbot, update_chatbot, delete_chatbot
import base64
from pro_dashboard import pro_dashboard
from promoter_dashboard import promoter_dashboard
import jwt  # Add this import for JWT handling
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(page_title="OmniJourney", page_icon="🧠", layout="wide")

# Selector de idioma con botones de bandera
col1, col2 = st.columns([1,19])
selected_language = st.session_state.get("language", "en")  # Default to English
with col1:
    if st.button("![ES](https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png)", key="spanish_button"):
        selected_language = "es"
with col2:        
    if st.button("![US](https://upload.wikimedia.org/wikipedia/en/a/a4/Flag_of_the_United_States.svg)", key="english_button"):
        selected_language = "en"

# Guardar idioma seleccionado en el estado de sesión
if "language" not in st.session_state:
    st.session_state.language = selected_language
elif st.session_state.language != selected_language:
    st.session_state.language = selected_language
    st.rerun()  # Recargar la página para aplicar el cambio de idioma

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

# Multilingual dictionary
translations = {
    "es": {
        "welcome_title": "🌟 Bienvenido a OmniJourney",
        "welcome_subtitle": "¡Explora el futuro de la interacción con IA!",
        "what_is_title": "¿Qué es OmniJourney?",
        "what_is_description": [
            "OmniJourney es una plataforma que conecta a los usuarios con chatbots personalizados, mejorando la experiencia digital.",
            "Nuestra misión es facilitar la interacción entre empresas, profesionales y usuarios a través de la inteligencia artificial.",
            "¡Únete a nosotros y descubre un mundo de posibilidades!"
        ],
        "login_prompt": "Inicia sesión para gestionar y descubrir chatbots personalizados que transformarán tu experiencia digital.",
        "email_label": "Correo electrónico",
        "password_label": "Contraseña",
        "login_button": "Iniciar sesión",
        "logout_button": "Cerrar sesión",
        "login_success": "Inicio de sesión exitoso",
        "login_error": "Correo o contraseña incorrectos",
        "footer": "© 2024 OmniJourney. Impulsado por IA."
    },
    "en": {
        "welcome_title": "🌟 Welcome to OmniJourney",
        "welcome_subtitle": "Explore the future of AI interaction!",
        "what_is_title": "What is OmniJourney?",
        "what_is_description": [
            "OmniJourney is a platform that connects users with personalized chatbots, enhancing the digital experience.",
            "Our mission is to facilitate interaction between businesses, professionals, and users through artificial intelligence.",
            "Join us and discover a world of possibilities!"
        ],
        "login_prompt": "Log in to manage and discover personalized chatbots that will transform your digital experience.",
        "email_label": "Email",
        "password_label": "Password",
        "login_button": "Log in",
        "logout_button": "Log out",
        "login_success": "Login successful",
        "login_error": "Incorrect email or password",
        "footer": "© 2024 OmniJourney. Powered by AI."
    }
}

# Function to get translated text
def t(key):
    return translations[st.session_state.language].get(key, key)

# Function to generate JWT token
def generate_jwt(email):
    secret_key = "your_secret_key"  # Replace with a secure key
    payload = {
        "email": email,
        "exp": datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
    }
    return jwt.encode(payload, secret_key, algorithm="HS256")

# Function to decode and verify JWT token
def verify_jwt(token):
    secret_key = "your_secret_key"  # Replace with the same secure key
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload["email"]
    except jwt.ExpiredSignatureError:
        st.error("Session expired. Please log in again.")
        return None
    except jwt.InvalidTokenError:
        st.error("Invalid token. Please log in again.")
        return None

# Estado de sesión
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.role = None

# Página de inicio de sesión
if not st.session_state.authenticated:
    col1, col2 = st.columns([4, 3])
    with col1:
        st.title(t("welcome_title"))
        st.subheader(t("welcome_subtitle"))
    with col2:
        with st.expander(t("what_is_title")):
            for line in t("what_is_description"):
                st.write(line)

        # Add buttons to redirect to WhatsApp
        if st.button(":red[Promocionar mi chat en la página]/:blue[Promote my chat on web page]"):
            st.markdown("[WhatsApp](https://wa.me/5930993513082?text=Quiero%20promocionar%20mi%20chat%20)", unsafe_allow_html=True)
        if st.button(":red[Registro como usuario]/:blue[User register]"):
            st.markdown("[WhatsApp](https://wa.me/5930993513082?text=Quiero%20ser%20usuario%20de%20los%20chats)", unsafe_allow_html=True)

    st.markdown(t("login_prompt"))
    email = st.text_input(t("email_label"))
    password = st.text_input(t("password_label"), type="password")
    if st.button(t("login_button")):
        user = authenticate_user(email, password)
        st.write(f"Debug: Resultado de authenticate_user: {user}")  # Mensaje de depuración
        if user:
            token = generate_jwt(email)  # Generate JWT token
            st.session_state.authenticated = True
            st.session_state.role = user["role"]
            st.session_state.token = token  # Store token in session state
            st.success(t("login_success"))
            st.rerun()
        else:
            st.error(t("login_error"))
else:
    # Redirigir según el rol
    if st.session_state.role == "admin":
        admin_dashboard()
    elif st.session_state.role == "basic":
        user_dashboard()
    elif st.session_state.role == "pro":
        pro_dashboard()
    elif st.session_state.role == "promoter":
        promoter_dashboard()

# Opción para cerrar sesión
if st.session_state.authenticated:
    email_from_token = verify_jwt(st.session_state.token)  # Verify JWT token
    if not email_from_token:
        st.session_state.authenticated = False
        st.session_state.role = None
        st.rerun()

# Pie de página
st.markdown("---")
st.caption(t("footer"))