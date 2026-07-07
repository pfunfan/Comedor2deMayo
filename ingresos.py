# Funcion para registrar ingresos
def registrar_ingreso(conn, cursor):
    # Preguntar datos
    fecha = input("Ingrese fecha (AAAA-MM-DD): \n")
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
    
    print("Ingreso guardado correctamente\n")

def mostrar_ingresos(cursor):
    # Leer datos (Selecciona todos los datos)
    cursor.execute("SELECT * FROM Ingresos")
    
    # Ver resultado
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)