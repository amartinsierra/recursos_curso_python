# Proyecto de análisis de ventas con Python

## Contenido
- `datos/ventas.csv`: 50 registros originales, con incidencias deliberadas.
- `app.py`: aplicación Streamlit.
- `servicios/`: carga, limpieza y análisis de datos.
- `paginas/`: vistas del dashboard.

## Ejecución en Windows (CMD)

Desde la carpeta `analisis_ventas`:

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app.py
```

Se abrirá la aplicación en el navegador. Para detenerla, pulsa Ctrl+C en la consola.

## Criterios de limpieza aplicados en la solución
1. Eliminar duplicados exactos.
2. Convertir fechas inválidas a `NaT` y descartar esas filas.
3. Convertir columnas numéricas y descartar filas con valores ausentes en campos necesarios.
4. Descartar unidades <= 0, precio <= 0, coste < 0 y descuentos fuera de [0, 100].
5. Calcular importe bruto, importe neto, coste total, beneficio y margen.

Las ventas estadísticamente atípicas se conservan. Se muestran en la sección Anomalías.

## Nota docente
Esta carpeta contiene una solución de referencia completa. Para entregar el ejercicio al alumnado, puedes proporcionar `datos/ventas.csv`, `requirements.txt` y el enunciado, sin entregar los módulos resueltos.
