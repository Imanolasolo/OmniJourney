import sqlite3
import bcrypt  # Add this import for password verification

# Función para ejecutar consultas (INSERT, UPDATE, DELETE)
def execute_query(query, params=None):
    conn = sqlite3.connect("omnijourney.db")
    try:
        conn.execute(query, params or ())
        conn.commit()
    finally:
        conn.close()

# Función para obtener resultados (SELECT)
def fetch_all(query, params=None):
    conn = sqlite3.connect("omnijourney.db")
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    try:
        cursor = conn.execute(query, params or ())
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()

# Función para conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect("omnijourney.db")
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return conn

# Placeholder for users_db (replace with actual database or data source)
users_db = [
    {"email": "admin@example.com", "password": "admin123", "role": "admin"},
    {"email": "user@example.com", "password": "user123", "role": "user"}
]

# Función para obtener todos los chatbots
def get_all_chatbots():
    conn = get_db_connection()
    chatbots = conn.execute("SELECT * FROM chatbots").fetchall()
    conn.close()
    return chatbots

# Función para insertar una interacción
def insert_interaction(chatbot_id, user_input, bot_response):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO interactions (chatbot_id, user_input, bot_response) VALUES (?, ?, ?)",
        (chatbot_id, user_input, bot_response)
    )
    conn.commit()
    conn.close()

# Función para autenticar usuarios
def authenticate_user(email, password):
    conn = sqlite3.connect("omnijourney.db")
    cursor = conn.cursor()
    cursor.execute("SELECT email, password, role FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode("utf-8"), user[1].encode("utf-8")):
        return {"email": user[0], "role": user[2]}
    return None

# Función para crear un chatbot
def create_chatbot(name, landing_page_url):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO chatbots (name, landing_page_url) VALUES (?, ?)",
        (name, landing_page_url)
    )
    conn.commit()
    conn.close()

# Función para actualizar un chatbot
def update_chatbot(chatbot_id, name, landing_page_url):
    conn = get_db_connection()
    conn.execute(
        "UPDATE chatbots SET name = ?, landing_page_url = ? WHERE id = ?",
        (name, landing_page_url, chatbot_id)
    )
    conn.commit()
    conn.close()

# Función para eliminar un chatbot
def delete_chatbot(chatbot_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM chatbots WHERE id = ?", (chatbot_id,))
    conn.commit()
    conn.close()