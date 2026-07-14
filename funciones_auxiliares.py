from datetime import datetime

# Solicita al usuario un monto y valida que la entrada sea un número decimal.
# Se utiliza para registrar valores monetarios como ingresos y egresos.
def pedir_monto(mensaje):
    while True:
        try:
            monto = input(mensaje)
            return float(monto)
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Solicita al usuario un número entero y valida que la entrada sea correcta.
# Se utiliza para IDs, opciones de menú y otras entradas numéricas enteras.
def pedir_entero(mensaje):
    while True:
        try:
            entero = input(mensaje)
            return int(entero)
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

# Solicita una confirmación al usuario y solo acepta las respuestas 's' o 'n'.
# Retorna la respuesta en minúscula para facilitar su comparación.
def pedir_confirmacion():
    while True:
        opcion = input("¿Desea continuar? (s/n): ").lower().strip() # Convierte a minuscula y quita espacios

        if opcion == "s" or opcion == "n":
            return opcion
        else:
            print("Error: Opción no válida.\n")

# Solicita un monto durante la edición de un registro.
# Permite dejar el campo vacío para conservar el valor actual.
# Si se ingresa un dato, valida que sea un número decimal.
def pedir_monto_opcional(mensaje, valor_actual):
    while True:
        try:
            dato = input(mensaje)
            
            if dato == "":
                return valor_actual
            return float(dato)
        except ValueError:
            print("Error: Debe ingresar un número válido.")

# Valida que una fecha tenga el formato AAAA-MM-DD.
# También verifica que la fecha exista realmente.
# Devuelve True si la fecha es válida y False en caso contrario.
def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False