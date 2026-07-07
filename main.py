from database import conectar, crear_tablas 
from ingresos import registrar_ingreso, mostrar_ingresos
from egresos import registrar_egreso, mostrar_egresos
from pdf import generar_pdf

# Conectarse a la base de datos
conn, cursor = conectar()

# Crear tabla si no existe
crear_tablas(cursor)

# Menu de opciones y programa
while True:
    print("""
    =========== COMEDOR POPULAR ===========
          
    1. Registrar Ingreso
    2. Registrar Egreso
    3. Mostrar Ingresos
    4. Mostrar Egresos
    5. Generar PDF
    6. Salir
    """)

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            registrar_ingreso(conn, cursor)
        case 2:
            registrar_egreso(conn, cursor)
        case 3:
            mostrar_ingresos(cursor)
        case 4:
            mostrar_egresos(cursor)
        case 5:
            month = int(input("Ingrese mes: \n"))
            year = int(input("Ingrese año: \n"))
            generar_pdf(conn, month, year)
        case 6:
            #Cerrar la conexión
            conn.close()
            break
        case _:
            print("Opcion no válida.")