def ingresos_encontrados(cursor, fecha):
    # Agrega '%' al final para buscar todas las fechas que comiencen
    # con el año y mes ingresados (Ejemplo: "2026-07%").
    patron_buscado = f"{fecha}%"

    # Ejecuta la consulta SQL.
    # '?' es un marcador de posición que será reemplazado por el valor
    # de 'patron_buscado' de forma segura.
    cursor.execute("SELECT * FROM Ingresos WHERE fecha LIKE ?", (patron_buscado,))

    # Obtiene todos los registros encontrados.
    # Si no existen coincidencias, devuelve una lista vacía ([]).
    ingresos = cursor.fetchall()

    # Una lista vacía se evalúa como False en Python.
    # Si no existen ingresos para el período solicitado, se informa al usuario.
    if not ingresos:
        print(f"No existen ingresos para el año y mes {patron_buscado}.")
    else:
        print("\n========== INGRESOS ==========\n")

        # Cada elemento de 'ingresos' es una tupla con este formato:
        # (id, fecha, nombre, baño, agua, papel)
        # Python asigna automáticamente cada columna a su variable.
        for _, fecha, nombre, baño, agua, papel in ingresos:

            # '_' recibe el ID del registro, pero no se utilizará.
            print(f"Fecha: {fecha} | Nombre: {nombre} | S/.Baño: {baño} | S/.Agua: {agua} | S/.Papel: {papel}")


def egresos_encontrados(cursor, fecha):
    # Agrega '%' al final para buscar todas las fechas que comiencen
    # con el año y mes ingresados (Ejemplo: "2026-07%").
    patron_buscado = f"{fecha}%"

    # Ejecuta la consulta SQL.
    # '?' es un marcador de posición que será reemplazado por el valor
    # de 'patron_buscado' de forma segura.
    cursor.execute("SELECT * FROM Egresos WHERE fecha LIKE ?", (patron_buscado,))

    # Obtiene todos los registros encontrados.
    # Si no existen coincidencias, devuelve una lista vacía ([]).
    egresos = cursor.fetchall()

    # Una lista vacía se evalúa como False en Python.
    # Si no existen egresos para el período solicitado, se informa al usuario.
    if not egresos:
        print(f"No existen egresos para el año y mes {patron_buscado}.")
    else:
        print("\n========== EGRESOS ==========\n")

        # Cada elemento de 'egresos' es una tupla con este formato:
        # (id, fecha, concepto, monto)
        # Python asigna automáticamente cada columna a su variable.
        for _, fecha, concepto, monto in egresos:

            # '_' recibe el ID del registro, pero no se utilizará.
            print(f"Fecha: {fecha} | Concepto: {concepto} | Monto: {monto}")