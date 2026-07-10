# Comedor Popular 2 de Mayo

Sistema desarrollado en **Python** para gestionar los ingresos y egresos del **Comedor Popular N°1 2 de Mayo**, utilizando una base de datos **SQLite** y generando reportes mensuales en **PDF**.

## Descripción

Este proyecto fue desarrollado como un proyecto personal con dos objetivos principales:

- Automatizar el registro de ingresos y egresos del comedor.
- Reforzar mis conocimientos de Python mediante el desarrollo de una aplicación real.

Toda la información se almacena en una base de datos SQLite y el sistema permite generar un reporte mensual en formato PDF con el resumen de ingresos y egresos.

## Capturas

### Menú principal

![Menú principal](screenshots/menu.png)

## Tecnologías utilizadas

- Python 3
- SQLite (`sqlite3`)
- ReportLab
- Git
- GitHub

## Funcionalidades

### Gestión de ingresos

- Registrar ingresos.
- Mostrar ingresos.
- Editar ingresos.
- Eliminar ingresos.

### Gestión de egresos

- Registrar egresos.
- Mostrar egresos.
- Editar egresos.
- Eliminar egresos.

### Reportes

- Generación de reportes mensuales en PDF.
- Consulta automática de ingresos y egresos según el mes seleccionado.
- Cálculo del total de ingresos y del total de egresos.
- Reporte dividido en dos páginas:
  - Ingresos.
  - Egresos.

## Estructura del proyecto

```text
ComedorPopular2deMayo/
│
├── main.py
├── database.py
├── ingresos.py
├── egresos.py
├── pdf.py
└── comedor.db
```

## Estado del proyecto

**Versión actual:** **v1.0**

El sistema cuenta con un CRUD completo para ingresos y egresos, almacenamiento en SQLite y generación de reportes mensuales en PDF.

## Próximas mejoras

- Validación de entradas del usuario.
- Manejo de errores mediante `try` y `except`.
- Búsqueda de ingresos y egresos.
- Mejoras en la presentación de los datos.
- Refactorización y optimización del código.

## Autor

Proyecto desarrollado por **Nano** como práctica personal de programación en Python y para automatizar la gestión del Comedor Popular N°1 2 de Mayo.
