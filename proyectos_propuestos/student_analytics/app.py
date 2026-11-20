import streamlit as st
import polars as pl

from notas_dao import obtener_notas
from analisis import (
    crear_dataframe,
    obtener_indicadores,
    medias_por_asignatura,
    distribucion_notas,
)

st.set_page_config(page_title="Student Analytics", page_icon="📚", layout="wide")
st.title("📚 Student Analytics")
st.caption("Consulta y análisis de calificaciones académicas")


def cargar_datos():
    return obtener_notas()


try:
    registros = cargar_datos()
    if not registros:
        st.warning("No hay calificaciones en la base de datos.")
        st.stop()

    df = crear_dataframe(registros)

    st.sidebar.header("Filtros")
    alumnos = ["Todos"] + sorted(df.get_column("alumno").unique().to_list())
    asignaturas = ["Todas"] + sorted(df.get_column("asignatura").unique().to_list())

    alumno_seleccionado = st.sidebar.selectbox("Alumno", alumnos)
    asignatura_seleccionada = st.sidebar.selectbox("Asignatura", asignaturas)
    nota_minima, nota_maxima = st.sidebar.slider(
        "Intervalo de notas", 0.0, 10.0, (0.0, 10.0), step=0.5
    )

    filtrado = df
    if alumno_seleccionado != "Todos":
        filtrado = filtrado.filter(pl.col("alumno") == alumno_seleccionado)
    if asignatura_seleccionada != "Todas":
        filtrado = filtrado.filter(pl.col("asignatura") == asignatura_seleccionada)

    filtrado = filtrado.filter(
        pl.col("nota").is_between(nota_minima, nota_maxima, closed="both")
    )

    st.subheader("Resumen")
    indicadores = obtener_indicadores(filtrado).row(0, named=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Alumnos", indicadores["alumnos"])
    c2.metric("Calificaciones", indicadores["calificaciones"])
    c3.metric("Nota media", f'{indicadores["media"]:.2f}')
    c4.metric("Aprobados", indicadores["aprobados"])

    st.subheader("Calificaciones")
    st.dataframe(
        filtrado.sort(["alumno", "asignatura", "fecha"]),
        hide_index=True,
        width="stretch",
    )

    izquierda, derecha = st.columns(2)
    with izquierda:
        st.subheader("Nota media por asignatura")
        medias = medias_por_asignatura(filtrado)
        if medias.height:
            st.bar_chart(medias, x="asignatura", y="nota_media")
        else:
            st.info("No hay datos para representar.")

    with derecha:
        st.subheader("Distribución de resultados")
        distribucion = distribucion_notas(filtrado)
        if distribucion.height:
            st.bar_chart(distribucion, x="intervalo", y="cantidad")
        else:
            st.info("No hay datos para representar.")

    st.caption(
        f'Suspensos: {indicadores["suspensos"]} · '
        f'Nota máxima: {indicadores["maxima"]:.2f} · '
        f'Nota mínima: {indicadores["minima"]:.2f}'
    )

except Exception as error:
    st.error("No se han podido cargar los datos.")
    st.exception(error)
    st.info(
        "Comprueba que MySQL está iniciado, que has ejecutado sql/inicializar.sql "
        "y que las variables de conexión son correctas."
    )
