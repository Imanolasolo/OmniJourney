import sqlite3
import bcrypt  # Add this import for password hashing

# Conexión a la base de datos SQLite
conn = sqlite3.connect("omnijourney.db")
cursor = conn.cursor()

# Eliminar la tabla de usuarios si ya existe (para recrearla con el nuevo CHECK constraint)
cursor.execute("DROP TABLE IF EXISTS users")

# Crear tabla de usuarios con el CHECK constraint actualizado
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT CHECK(role IN ('admin', 'basic', 'pro', 'promoter')) NOT NULL DEFAULT 'basic',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Crear tabla de chatbots
cursor.execute("""
CREATE TABLE IF NOT EXISTS chatbots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    api_key TEXT,
    status TEXT CHECK(status IN ('active', 'inactive')) DEFAULT 'inactive',
    knowledge_base TEXT,
    landing_page_url TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

# Crear tabla de interacciones
cursor.execute("""
CREATE TABLE IF NOT EXISTS interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chatbot_id INTEGER,
    user_input TEXT,
    bot_response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (chatbot_id) REFERENCES chatbots(id)
)
""")

# Hash the admin password before inserting
admin_password = bcrypt.hashpw("admin123".encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

# Insertar un usuario administrador hardcodeado
cursor.execute("""
INSERT OR IGNORE INTO users (username, email, password, role)
VALUES ('admin', 'admin@example.com', ?, 'admin')
""", (admin_password,))

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos y tablas creadas exitosamente.")