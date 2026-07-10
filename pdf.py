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
    return ingresos

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
    return egresos

def generar_pdf(cursor):
    año = input("Año(AAAA): ")
    mes = input("Mes(MM): ")
    print("")

    mes = mes.zfill(2)
    fecha = f"{año}-{mes}"

    ingresos = ingresos_encontrados(cursor, fecha)
    egresos = egresos_encontrados(cursor, fecha)

    if not ingresos:
        print(f"No existen ingresos para el año y mes {fecha}.")
    else:
        print(f"Se encontraron {len(ingresos)} ingresos en {fecha}.")
        
        total_ingresos = 0
        for _, _, _, baño, agua, papel in ingresos:
            total_ingreso = baño + agua + papel
            total_ingresos += total_ingreso
        print(f"Total ingresos: S/. {total_ingresos}\n")
    
    if not egresos:
        print(f"No existen egresos para el año y mes {fecha}.")
    else:
        print(f"Se encontraron {len(egresos)} egresos en {fecha}.")

        total_egresos = 0
        for _, _, _, monto in egresos:
            total_egresos += monto
        print(f"Total egresos: S/. {total_egresos}")