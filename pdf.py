from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Función para generar el PDF
def generar_pdf(conn, month, year):
    # Meses
    match month:
        case 1:
            nombre_mes = "ENERO"
        case 2:
            nombre_mes = "FEBRERO"
        case 3:
            nombre_mes = "MARZO"
        case 4:
            nombre_mes = "ABRIL"
        case 5:
            nombre_mes = "MAYO"
        case 6:
            nombre_mes = "JUNIO"
        case 7:
            nombre_mes = "JULIO"
        case 8:
            nombre_mes = "AGOSTO"
        case 9:
            nombre_mes = "SETIEMBRE"
        case 10:
            nombre_mes = "OCTUBRE"
        case 11:
            nombre_mes = "NOVIEMBRE"
        case 12:
            nombre_mes = "DICIEMBRE"
        case _:
            nombre_mes = "MES DESCONOCIDO"

    # Nombre del archivo PDF y tamaño de la página
    documento = SimpleDocTemplate("reporte.pdf", pagesize=letter)

    # Obtener estilos predeterminados de ReportLab
    estilos = getSampleStyleSheet()

    # Lista donde se agregan todos los elementos que aparecerán en el PDF
    contenido = []

    titulo = f"INGRESOS {nombre_mes} {year} (BAÑO)"

    # Agregar un título al documento
    text = Paragraph(titulo, estilos["Title"])
    contenido.append(text)

    # Construir y guardar el PDF
    documento.build(contenido)

    print("PDF generado correctamente.")