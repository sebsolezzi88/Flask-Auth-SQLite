import os
import sqlite3
from dotenv import load_dotenv

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