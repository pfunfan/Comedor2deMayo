from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.platypus import Spacer
from reportlab.platypus import PageBreak

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

# 'fecha[-2:]' obtiene los dos últimos caracteres de la cadena.
# Como la fecha tiene el formato "AAAA-MM", los dos últimos caracteres
# corresponden al número del mes.
# Ejemplos:
# "2026-01" -> "01"
# "2026-07" -> "07"
# "2026-12" -> "12"
def fecha_texto(fecha):
    if fecha[-2:] == "01":
        return "ENERO"
    elif fecha[-2:] == "02":
        return "FEBRERO"
    elif fecha[-2:] == "03":
        return "MARZO"
    elif fecha[-2:] == "04":
        return "ABRIL"
    elif fecha[-2:] == "05":
        return "MAYO"
    elif fecha[-2:] == "06":
        return "JUNIO"
    elif fecha[-2:] == "07":
        return "JULIO"
    elif fecha[-2:] == "08":
        return "AGOSTO"
    elif fecha[-2:] == "09":
        return "SETIEMBRE"
    elif fecha[-2:] == "10":
        return "OCTUBRE"
    elif fecha[-2:] == "11":
        return "NOVIEMBRE"
    elif fecha[-2:] == "12":
        return "DICIEMBRE"

def total_ingresos_egresos(ingresos, egresos):
    total_ingresos = 0

    for _, _, _, baño, agua, papel in ingresos:
        total_ingreso = baño + agua + papel
        total_ingresos += total_ingreso
    
    total_egresos = 0
    for _, _, _, monto in egresos:
        total_egresos += monto
    
    return total_ingresos, total_egresos

def crear_listas_de_datos(ingresos, egresos):

    i, e = total_ingresos_egresos(ingresos, egresos)

    # Lista para ingresos
    datos_ingresos = [
        ["Fecha", "Nombre", "S/.Baño", "S/.Agua", "S/.Papel", "S/.Total"],
    ]

    for _, fecha, nombre, baño, agua, papel in ingresos:
        total = baño + agua + papel
        fila = [fecha, nombre, f"{baño:.2f}", f"{agua:.2f}", f"{papel:.2f}", f"{total:.2f}"]
        datos_ingresos.append(fila)
    datos_ingresos.append(["", "", "", "", "S/.TOTAL", f"{i:.2f}"])

    # Lista para egresos
    datos_egresos = [
        ["Fecha", "Concepto", "S/.Monto"]
    ]

    for _, fecha, concepto, monto in egresos:
        fila = [fecha, concepto, f"{monto:.2f}"]
        datos_egresos.append(fila)
    datos_egresos.append(["", "S/.TOTAL", f"{e:.2f}"])

    return datos_ingresos, datos_egresos

def crear_tablas_pdf(datos_ingresos, datos_egresos, elementos):
    tabla_ingresos = Table(datos_ingresos)
    tabla_ingresos.setStyle(
        TableStyle([
            # Configura los bordes de la tabla completa
            # Sintaxis: ("ESTILO", (Col,Fila_Inicio), (Col,Fila_Fin), Grosor, Color), (c, f)
            ("GRID", (0, 0), (-1, -1), 1.5, colors.black),
            # Fondo Teal solo para la primera fila (encabezado) desde la col 0 hasta la última (-1)
            ("BACKGROUND", (0, 0), (-1, 0), colors.teal),
            # Letra blanca solo para la primera fila (encabezado) desde la col 0 hasta la última (-1)
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            # Texto en negrita (Helvetica-Bold) solo para los títulos de la primera fila
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            # Alinear los valores de baño, agua y papel a la derecha
            ("ALIGN", (2, 1), (-1, -1), "RIGHT"),
            # Alinea valores de primera fila al centro (encabezado)
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            # Alinea verticalmente todo al centro
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            # Agrega 8 puntos de separación entre el texto y el borde de abajo (solo encabezado)
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            # Agrega tamaño de letra a toda la tabla
            ("FONTSIZE", (0, 0), (-1, -1), 11)
        ])
    )

    tabla_egresos = Table(datos_egresos)
    tabla_egresos.setStyle(
        TableStyle([
            # Configura los bordes de la tabla completa
            # Sintaxis: ("ESTILO", (Col,Fila_Inicio), (Col,Fila_Fin), Grosor, Color), (c, f)
            ("GRID", (0, 0), (-1, -1), 1.5, colors.black),
            # Fondo Teal solo para la primera fila (encabezado) desde la col 0 hasta la última (-1)
            ("BACKGROUND", (0, 0), (-1, 0), colors.teal),
            # Letra blanca solo para la primera fila (encabezado) desde la col 0 hasta la última (-1)
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            # Texto en negrita (Helvetica-Bold) solo para los títulos de la primera fila
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            # Alinear monto a la derecha
            ("ALIGN", (-1, 1), (-1, -1), "RIGHT"),
            # Alinea valores de primera fila al centro (encabezado)
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            # Alinea verticalmente todo al centro
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            # Agrega 8 puntos de separación entre el texto y el borde de abajo (solo encabezado)
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            # Agrega tamaño de letra a toda la tabla
            ("FONTSIZE", (0, 0), (-1, -1), 11)
        ])
    )
    return tabla_ingresos, tabla_egresos
    
def crear_pdf(fecha, ingresos, egresos):
    # Crea el documento PDF.
    doc = SimpleDocTemplate(f"{fecha}.pdf")

    # Lista donde se irán agregando todos los elementos del PDF
    elementos = []

    # Obtiene los estilos predeterminados de ReportLab.
    estilos = getSampleStyleSheet()

    # Titulo para ingresos
    texto_ingresos = (
        f"COMEDOR POPULAR N°1 (2 DE MAYO)<br/><br/>"
        f"INGRESOS REPORTE MENSUAL<br/>"
        f"{fecha_texto(fecha)} {fecha[:4]}"
    )

    datos_ingresos, datos_egresos = crear_listas_de_datos(ingresos, egresos)

    # Parrafo y agregarlo a la lista para la primera hoja
    encabezado = Paragraph(texto_ingresos, estilos["Title"])
    elementos.append(encabezado)

    # Espacio entre titulo y tabla Spacer(ancho, alto)
    elementos.append(Spacer(1, 20))

    # Implementacion de tabla ingresos con su diseño
    tabla_ingresos, tabla_egresos = crear_tablas_pdf(datos_ingresos, datos_egresos, elementos)
    elementos.append(tabla_ingresos)

    # Nueva hoja
    elementos.append(PageBreak())

    # Titulo para egresos
    texto_egresos = (
        f"COMEDOR POPULAR N°1 (2 DE MAYO)<br/><br/>"
        f"EGRESOS REPORTE MENSUAL<br/>"
        f"{fecha_texto(fecha)} {fecha[:4]}"
    )

    # Parrafo y agregarlo a la lista para la segunda hoja
    encabezado = Paragraph(texto_egresos, estilos["Title"])
    elementos.append(encabezado)

    # Espacio entre titulo y tabla Spacer(ancho, alto)
    elementos.append(Spacer(1, 20))

    # Implementacion de tablas egresos con su diseño
    elementos.append(tabla_egresos)

    # Construye el PDF utilizando los elementos de la lista.
    doc.build(elementos)

def generar_pdf(cursor):
    año = input("Año(AAAA): ")
    mes = input("Mes(MM): ")
    print("")

    mes = mes.zfill(2)
    fecha = f"{año}-{mes}"

    ingresos = ingresos_encontrados(cursor, fecha)
    egresos = egresos_encontrados(cursor, fecha)

    if not ingresos and not egresos:
        print(f"No existen ingresos ni egresos en el año {fecha}.")
    else:
        crear_pdf(fecha, ingresos, egresos)
        print("PDF generado exitosamente.")