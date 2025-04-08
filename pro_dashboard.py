import streamlit as st

# Diccionario de traducciones
translations = {
    "es": {
        "title": "💼 Panel Pro",
        "welcome": "Bienvenido al panel Pro. Aquí puedes gestionar tus funcionalidades avanzadas.",
        "features_title": "⚙️ Funcionalidades Avanzadas",
        "feature_1": "1. Analítica avanzada de chatbots.",
        "feature_2": "2. Personalización de respuestas.",
        "feature_3": "3. Integración con herramientas externas."
    },
    "en": {
        "title": "💼 Pro Dashboard",
        "welcome": "Welcome to the Pro Dashboard. Here you can manage your advanced features.",
        "features_title": "⚙️ Advanced Features",
        "feature_1": "1. Advanced chatbot analytics.",
        "feature_2": "2. Response customization.",
        "feature_3": "3. Integration with external tools."
    }
}

def pro_dashboard():
    # Obtener traducciones según el idioma seleccionado
    selected_language = st.session_state.get("language", "es")  # Valor predeterminado: "es"
    t = translations[selected_language]

    st.title(t["title"])
    st.write(t["welcome"])
    st.subheader(t["features_title"])
    st.write(t["feature_1"])
    st.write(t["feature_2"])
    st.write(t["feature_3"])

    # Add logout button at the end of the Pro dashboard
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.role = None
        st.rerun()
