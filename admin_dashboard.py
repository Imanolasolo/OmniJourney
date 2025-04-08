import streamlit as st
import bcrypt  # Add this import for password hashing
from database.database import get_all_chatbots, authenticate_user, create_chatbot, update_chatbot, delete_chatbot
from database.user_crud import create_user, get_all_users, update_user, delete_user

# Diccionario de traducciones
translations = {
    "es": {
        "title": "👨‍💼 Panel de Administrador",
        "welcome": "Bienvenido al panel de administración.",
        "chatbot_management": "### 🛠️ Gestión de Chatbots",
        "user_management": "### 👥 Gestión de Usuarios",
        "select_action_chatbots": "Seleccionar acción para Chatbots",
        "select_action_users": "Seleccionar acción para Usuarios",
        "create": "Crear",
        "read": "Leer",
        "update": "Actualizar",
        "delete": "Eliminar",
        "create_chatbot": "Crear Chatbot",
        "chatbot_name": "Nombre del Chatbot",
        "chatbot_url": "URL del Chat",
        "save": "Guardar",
        "chatbot_created": "Chatbot creado exitosamente.",
        "list_chatbots": "Lista de Chatbots",
        "url": "URL",
        "update_chatbot": "Actualizar Chatbot",
        "select_chatbot": "Seleccionar Chatbot",
        "new_name": "Nuevo Nombre",
        "new_url": "Nueva URL del Chat",
        "chatbot_updated": "Chatbot actualizado exitosamente.",
        "delete_chatbot": "Eliminar Chatbot",
        "chatbot_deleted": "Chatbot eliminado exitosamente.",
        "create_user": "Crear Usuario",
        "username": "Nombre de Usuario",
        "email": "Correo Electrónico",
        "password": "Contraseña",
        "save_user": "Guardar Usuario",
        "user_created": "Usuario creado exitosamente.",
        "list_users": "Lista de Usuarios",
        "update_user": "Actualizar Usuario",
        "select_user": "Seleccionar Usuario",
        "new_username": "Nuevo Nombre",
        "new_email": "Nuevo Correo Electrónico",
        "new_password": "Nueva Contraseña (opcional)",
        "user_updated": "Usuario actualizado exitosamente.",
        "delete_user": "Eliminar Usuario",
        "user_deleted": "Usuario eliminado exitosamente."
    },
    "en": {
        "title": "👨‍💼 Admin Dashboard",
        "welcome": "Welcome to the admin dashboard.",
        "chatbot_management": "### 🛠️ Chatbot Management",
        "user_management": "### 👥 User Management",
        "select_action_chatbots": "Select action for Chatbots",
        "select_action_users": "Select action for Users",
        "create": "Create",
        "read": "Read",
        "update": "Update",
        "delete": "Delete",
        "create_chatbot": "Create Chatbot",
        "chatbot_name": "Chatbot Name",
        "chatbot_url": "Chat URL",
        "save": "Save",
        "chatbot_created": "Chatbot created successfully.",
        "list_chatbots": "List of Chatbots",
        "url": "URL",
        "update_chatbot": "Update Chatbot",
        "select_chatbot": "Select Chatbot",
        "new_name": "New Name",
        "new_url": "New Chat URL",
        "chatbot_updated": "Chatbot updated successfully.",
        "delete_chatbot": "Delete Chatbot",
        "chatbot_deleted": "Chatbot deleted successfully.",
        "create_user": "Create User",
        "username": "Username",
        "email": "Email",
        "password": "Password",
        "save_user": "Save User",
        "user_created": "User created successfully.",
        "list_users": "List of Users",
        "update_user": "Update User",
        "select_user": "Select User",
        "new_username": "New Username",
        "new_email": "New Email",
        "new_password": "New Password (optional)",
        "user_updated": "User updated successfully.",
        "delete_user": "Delete User",
        "user_deleted": "User deleted successfully."
    }
}

def admin_dashboard():
    # Eliminar botones para cambiar el idioma, ya que están en app.py

    # Obtener traducciones según el idioma seleccionado
    selected_language = st.session_state.get("language", "es")  # Valor predeterminado: "es"
    t = translations[selected_language]

    st.title(t["title"])
    st.write(t["welcome"])
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(t["chatbot_management"])
        with st.expander(t["chatbot_management"], expanded=False):
            action = st.selectbox(t["select_action_chatbots"], [t["create"], t["read"], t["update"], t["delete"]])
        
            if action == t["create"]:
                st.subheader(t["create_chatbot"])
                name = st.text_input(t["chatbot_name"])
                landing_page_url = st.text_input(t["chatbot_url"])
                if st.button(t["save"]):
                    create_chatbot(name, landing_page_url)
                    st.success(t["chatbot_created"])
        
            elif action == t["read"]:
                st.subheader(t["list_chatbots"])
                chatbots = get_all_chatbots()
                for chatbot in chatbots:
                    st.write(f"**{chatbot['name']}** - {t['url']}: {chatbot['landing_page_url']}")
        
            elif action == t["update"]:
                st.subheader(t["update_chatbot"])
                chatbots = get_all_chatbots()
                chatbot_names = [chatbot['name'] for chatbot in chatbots]
                selected_chatbot = st.selectbox(t["select_chatbot"], chatbot_names)
                if selected_chatbot:
                    chatbot = next(c for c in chatbots if c['name'] == selected_chatbot)
                    new_name = st.text_input(t["new_name"], chatbot['name'])
                    new_landing_page_url = st.text_input(t["new_url"], chatbot['landing_page_url'])
                    if st.button(t["update"]):
                        update_chatbot(chatbot['id'], new_name, new_landing_page_url)
                        st.success(t["chatbot_updated"])
        
            elif action == t["delete"]:
                st.subheader(t["delete_chatbot"])
                chatbots = get_all_chatbots()
                chatbot_names = [chatbot['name'] for chatbot in chatbots]
                selected_chatbot = st.selectbox(t["select_chatbot"], chatbot_names)
                if selected_chatbot:
                    chatbot = next(c for c in chatbots if c['name'] == selected_chatbot)
                    if st.button(t["delete"]):
                        delete_chatbot(chatbot['id'])
                        st.success(t["chatbot_deleted"])
    with col2:
        st.markdown(t["user_management"])
        with st.expander(t["user_management"], expanded=False):
            user_action = st.selectbox(t["select_action_users"], [t["create"], t["read"], t["update"], t["delete"]], key="user_action")
    
            if user_action == t["create"]:
                st.subheader(t["create_user"])
                username = st.text_input(t["username"])
                email = st.text_input(t["email"])
                password = st.text_input(t["password"], type="password")
                role = st.selectbox("Role", ["admin", "basic", "pro", "promoter"])  # Add role selection
                if st.button(t["save_user"]):
                    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")  # Hash the password
                    create_user(username, email, hashed_password, role)  # Pass hashed password to create_user
                    st.success(t["user_created"])
    
            elif user_action == t["read"]:
                st.subheader(t["list_users"])
                users = get_all_users()
                for user in users:
                    st.write(f"**{user['username']}** - {t['email']}: {user['email']}")
    
            elif user_action == t["update"]:
                st.subheader(t["update_user"])
                users = get_all_users()
                user_names = [user['username'] for user in users]
                selected_user = st.selectbox(t["select_user"], user_names)
                if selected_user:
                    user = next(u for u in users if u['username'] == selected_user)
                    new_username = st.text_input(t["new_username"], user['username'])
                    new_email = st.text_input(t["new_email"], user['email'])
                    new_password = st.text_input(t["new_password"], type="password")
                    role = st.selectbox(
                        "Role",
                        ["admin", "basic", "pro", "promoter"],
                        index=["admin", "basic", "pro", "promoter"].index(user.get("role", "basic"))  # Fallback to "basic"
                    )
                    if st.button(t["update_user"]):
                        hashed_password = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8") if new_password else None
                        update_user(user['id'], new_username, new_email, hashed_password, role)  # Pass hashed password if provided
                        st.success(t["user_updated"])
    
            elif user_action == t["delete"]:
                st.subheader(t["delete_user"])
                users = get_all_users()
                user_names = [user['username'] for user in users]
                selected_user = st.selectbox(t["select_user"], user_names)
                if selected_user:
                    user = next(u for u in users if u['username'] == selected_user)
                    if st.button(t["delete_user"]):
                        delete_user(user['id'])
                        st.success(t["user_deleted"])

    # Add logout button at the end of the admin dashboard
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.role = None
        st.rerun()