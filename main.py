from database import conectar, crear_tablas 
from ingresos import registrar_ingreso, mostrar_ingresos

# Conectarse a la base de datos
conn, cursor = conectar()

# Crear tabla si no existe
crear_tablas(cursor)

# Menu de opciones y programa
while True:
    print("""
    =========== COMEDOR POPULAR ===========
          
    1. Registrar ingreso
    2. Mostrar ingresos
    3. Salir
    """)

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            registrar_ingreso(conn, cursor)
        case 2:
            mostrar_ingresos(cursor)
        case 3:
            #Cerrar la conexión
            conn.close()
            break
        case _:
            print("Opcion no válida.")
            