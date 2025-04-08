import streamlit as st

# Diccionario de traducciones
translations = {
    "es": {
        "title": "📢 Panel Promoter",
        "welcome": "Bienvenido al panel Promoter. Aquí puedes gestionar tus campañas de promoción.",
        "features_title": "📈 Funcionalidades de Promoción",
        "feature_1": "1. Creación de campañas promocionales.",
        "feature_2": "2. Seguimiento de métricas de rendimiento.",
        "feature_3": "3. Optimización de estrategias de marketing."
    },
    "en": {
        "title": "📢 Promoter Dashboard",
        "welcome": "Welcome to the Promoter Dashboard. Here you can manage your promotion campaigns.",
        "features_title": "📈 Promotion Features",
        "feature_1": "1. Creation of promotional campaigns.",
        "feature_2": "2. Tracking performance metrics.",
        "feature_3": "3. Optimizing marketing strategies."
    }
}

def promoter_dashboard():
    # Obtener traducciones según el idioma seleccionado
    selected_language = st.session_state.get("language", "es")  # Valor predeterminado: "es"
    t = translations[selected_language]

    st.title(t["title"])
    st.write(t["welcome"])
    st.subheader(t["features_title"])
    st.write(t["feature_1"])
    st.write(t["feature_2"])
    st.write(t["feature_3"])

    # Add logout button at the end of the Promoter dashboard
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.role = None
        st.rerun()
