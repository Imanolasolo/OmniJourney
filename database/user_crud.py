from database.database import execute_query, fetch_all

def create_user(username, email, password, role='user'):
    query = """
    INSERT INTO users (username, email, password, role)
    VALUES (?, ?, ?, ?)
    """
    execute_query(query, (username, email, password, role))

def get_all_users():
    query = "SELECT id, username, email FROM users"
    return fetch_all(query)

def update_user(user_id, username, email, password=None, role=None):
    query = "UPDATE users SET username = ?, email = ?"
    params = [username, email]
    
    if password:
        query += ", password = ?"
        params.append(password)
    
    if role:
        query += ", role = ?"
        params.append(role)
    
    query += " WHERE id = ?"
    params.append(user_id)
    
    execute_query(query, tuple(params))

def delete_user(user_id):
    query = "DELETE FROM users WHERE id = ?"
    execute_query(query, (user_id,))
