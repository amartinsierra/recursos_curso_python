# Student Analytics

Pequeña aplicación de análisis de calificaciones con Python, MySQL, Polars y Streamlit.

## 1. Requisitos

- Python 3.10 o posterior.
- MySQL en ejecución.
- Una base de datos local o accesible desde el equipo.

## 2. Crear la base de datos y los datos de prueba

Ejecuta el contenido de `sql/inicializar.sql` desde MySQL Workbench, DBeaver o la consola de MySQL.

El script crea la base de datos `student_analytics`, una única tabla (`notas`) e inserta 100 calificaciones ficticias.

## 3. Instalar dependencias

Desde la carpeta del proyecto:

```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 4. Configurar la conexión

Por defecto, la aplicación intenta conectarse a:

- Host: `localhost`
- Puerto: `3306`
- Usuario: `root`
- Contraseña: vacía
- Base de datos: `student_analytics`

Puedes cambiar estos valores mediante variables de entorno en Windows CMD. Por ejemplo:

```cmd
set MYSQL_HOST=localhost
set MYSQL_PORT=3306
set MYSQL_USER=root
set MYSQL_PASSWORD=tu_clave
set MYSQL_DATABASE=student_analytics
```

Estas variables solo permanecen definidas en esa ventana de CMD.

## 5. Ejecutar

```cmd
streamlit run app.py
```

## 6. Qué hace cada módulo

- `conexion.py`: abre la conexión con MySQL.
- `notas_dao.py`: ejecuta el SELECT y devuelve una lista de diccionarios.
- `analisis.py`: convierte los registros en un DataFrame de Polars y calcula estadísticas.
- `app.py`: presenta filtros, tabla, indicadores y gráficos.

Los gráficos utilizan `st.bar_chart` de Streamlit para mantener el proyecto pequeño y evitar código adicional de Matplotlib.

## 7. Estructura

```text
student_analytics/
├── app.py
├── analisis.py
├── conexion.py
├── notas_dao.py
├── requirements.txt
├── README.md
└── sql/
    └── inicializar.sql
```
