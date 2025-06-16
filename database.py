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
    
def buscar_username_password(username):
    with sqlite3.connect(os.environ.get('DATABASE_PATH')) as conn:
        conn.row_factory = sqlite3.Row #para que regrese un diccionario
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?;",(username,))
        user = cursor.fetchone()
        return user


def buscar_tareas_por_user_id(userid):
    with sqlite3.connect(os.environ.get('DATABASE_PATH')) as conn:
        conn.row_factory = sqlite3.Row #para que regrese un diccionario
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tareas WHERE user_id = ?",(userid,))
        tareas = cursor.fetchall()
        return tareas
    

def agregar_tarea(titulo,descripcion,user_id):
    with sqlite3.connect(os.environ.get('DATABASE_PATH')) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tareas (titulo, descripcion, user_id) VALUES (?,?,?) ",(titulo,descripcion,user_id))