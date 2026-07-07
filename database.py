import sqlite3

def conectar():
    # Conectar a la base de datos
    conn = sqlite3.connect("comedor.db")
    print("Conectado a la base de datos.")

    # Crear el cursor para ejecutar diferentes acciones
    cursor = conn.cursor()

    # Retornar conn y cursor para no repetir codigo
    return conn, cursor

def crear_tablas(cursor):
    # Crear tabla Ingresos y Egresos
    cursor.execute("""CREATE TABLE IF NOT EXISTS Ingresos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                nombre TEXT,
                baño REAL,
                agua REAL,
                papel REAL                  
    )
    """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS Egresos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                concepto TEXT,
                monto REAL               
    )
    """)