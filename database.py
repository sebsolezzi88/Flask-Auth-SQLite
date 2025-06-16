import os
import sqlite3
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

#Cargar variable de entorno
load_dotenv()


#Crear base de datos
def crear_data_base():
    with sqlite3.connect(os.environ.get('DATABASE_PATH')) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        ''')

#Inserta usuario
def insertar_usuario(username,password):
    #hashear password
    passwordhash = generate_password_hash(password)
    with sqlite3.connect(os.environ.get('DATABASE_PATH')) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?);",(username,passwordhash))

def buscar_username(username):
    with sqlite3.connect(os.environ.get('DATABASE_PATH')) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM users WHERE username = ?;",(username,))
        user = cursor.fetchone()
        return user