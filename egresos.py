# Funcion para registrar egresos
def registrar_egreso(conn, cursor):
    # Preguntar datos
    fecha = input("Ingrese fecha: \n")
    concepto = input("Ingrese concepto: \n")
    monto = float(input("Ingrese el monto: \n"))
    
    # Tupla para insertar valores a la tabla
    tupla = (fecha, concepto, monto)

    # Insertar valores
    cursor.execute("""INSERT INTO Egresos (fecha, concepto, monto)
         VALUES (?, ?, ?)""", tupla)
    
    # Guardar cambios
    conn.commit()
    
    print("Egreso guardado correctamente\n")

def mostrar_egresos(cursor):
    # Leer datos (Selecciona todos los datos)
    cursor.execute("SELECT * FROM Egresos")
    
    # Ver resultado
    egresos = cursor.fetchall()
    for egreso in egresos:
        print(egreso)