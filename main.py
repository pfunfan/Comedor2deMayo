from database import conectar, crear_tablas 

# Conectarse a la base de datos
conn, cursor = conectar()

# Crear tabla si no existe
crear_tablas(cursor)

# Funcion para registrar ingresos
def registrar_ingreso():
    # Preguntar datos
    fecha = input("Ingrese fecha: \n")
    nombre = input("Ingrese nombre: \n")
    baño = float(input("Ingrese monto del baño: \n"))
    agua = float(input("Ingrese monto del agua: \n"))
    papel = float(input("Ingrese monto del papel: \n"))
    
    # Tupla para insertar valores a la tabla
    tupla = (fecha, nombre, baño, agua, papel)

    # Insertar valores
    cursor.execute("""INSERT INTO Ingresos (fecha, nombre, baño, agua, papel)
         VALUES (?, ?, ?, ?, ?)""", tupla)
    
    # Guardar cambios
    conn.commit()
    
    print("Ingreso guardado correctamente")

def mostrar_ingresos():
    # Leer datos (Selecciona todos los datos)
    cursor.execute("SELECT * FROM Ingresos")
    
    # Ver resultado
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

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
            registrar_ingreso()
        case 2:
            mostrar_ingresos()
        case 3:
            #Cerrar la conexión
            conn.close()
            break
        case _:
            print("Opcion no válida.")
            