# Biblioteca: Python + MySQL

## Preparación
1. Ejecuta `sql/01_creacion.sql` en MySQL Workbench.
2. Ejecuta `sql/02_datos_iniciales.sql`.
3. Edita `conexion.py` y sustituye `TU_PASSWORD` por la contraseña de MySQL.

## Instalación y ejecución (Windows CMD)
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Archivos
- `conexion.py`: conexión a MySQL.
- `libros.py`: operaciones de libros.
- `socios.py`: operaciones de socios.
- `prestamos.py`: préstamos, devoluciones y consultas.
- `app.py`: menú de consola.

La solución utiliza consultas parametrizadas (`%s`) y transacciones para que el alta de un préstamo y la actualización de disponibilidad se confirmen o deshagan conjuntamente.
