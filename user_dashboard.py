import streamlit as st
from database.database import get_all_chatbots, authenticate_user, create_chatbot, update_chatbot, delete_chatbot

# Diccionario de traducciones
translations = {
    "es": {
        "title": "👤 Panel de Usuario",
        "welcome": "Bienvenido al panel de usuario.",
        "links": "### 🌐 Enlaces a Chatbots",
        "no_chatbots": "No hay chatbots disponibles en este momento.",
        "features_title": "🔧 Funcionalidades del Usuario",
        "feature_1": "1. Acceso a chatbots personalizados.",
        "feature_2": "2. Gestión de perfiles de usuario.",
        "feature_3": "3. Historial de interacciones."
    },
    "en": {
        "title": "👤 User Dashboard",
        "welcome": "Welcome to the user dashboard.",
        "links": "### 🌐 Chatbot Links",
        "no_chatbots": "No chatbots available at the moment.",
        "features_title": "🔧 User Features",
        "feature_1": "1. Access to personalized chatbots.",
        "feature_2": "2. User profile management.",
        "feature_3": "3. Interaction history."
    }
}

def user_dashboard():
    # Eliminar botones para cambiar el idioma, ya que están en app.py

    # Obtener traducciones según el idioma seleccionado
    selected_language = st.session_state.get("language", "es")  # Valor predeterminado: "es"
    t = translations[selected_language]

    st.title(t["title"])
    st.write(t["welcome"])
        
    # Mostrar enlaces a las landing pages de los chatbots
    st.markdown(t["links"])
    chatbots = get_all_chatbots()
    if chatbots:
        for chatbot in chatbots:
            st.markdown(f"- [{chatbot['name']}]({chatbot['landing_page_url']})")
    else:
        st.write(t["no_chatbots"])

    st.subheader(t["features_title"])
    st.write(t["feature_1"])
    st.write(t["feature_2"])
    st.write(t["feature_3"])

    # Add logout button at the end of the user dashboard
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.role = None
        st.rerun()