import streamlit as st

import negocio
import graficos


st.set_page_config(
    page_title="Análisis académico",
    page_icon="📊",
    layout="wide"
)


#@st.cache_data
def cargar_informacion():

    alumnos, notas = negocio.cargar_datos()

    return negocio.obtener_notas_completas(
        alumnos, notas
    )


datos = cargar_informacion()

st.sidebar.title("Filtros")

cursos = ["Todos"] + sorted(
    datos["curso"].unique().to_list()
)

asignaturas = ["Todas"] + sorted(
    datos["asignatura"].unique().to_list()
)

grupos = ["Todos"] + sorted(
    datos["grupo"].unique().to_list()
)

evaluaciones = ["Todas"] + sorted(
    datos["evaluacion"].unique().to_list()
)


curso = st.sidebar.selectbox(
    "Curso",
    cursos
)

asignatura = st.sidebar.selectbox(
    "Asignatura",
    asignaturas
)

grupo = st.sidebar.selectbox(
    "Grupo",
    grupos
)

evaluacion = st.sidebar.selectbox(
    "Evaluación",
    evaluaciones
)

datos_filtrados = negocio.filtrar_notas(
    datos,
    curso,
    asignatura,
    evaluacion,
    grupo
)
st.title("📊 Dashboard de rendimiento académico")

if datos_filtrados.is_empty():

    st.warning("No existen resultados para los filtros seleccionados.")

    st.stop()
    
indicadores = negocio.obtener_indicadores(
    datos_filtrados
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Alumnos evaluados",
    indicadores["alumnos"]
)

col2.metric(
    "Nota media",
    f"{indicadores['media']:.2f}"
)

col3.metric(
    "Nota máxima",
    f"{indicadores['maxima']:.2f}"
)

col4.metric(
    "Nota mínima",
    f"{indicadores['minima']:.2f}"
)

col5.metric(
    "Aprobados",
    f"{indicadores['porcentaje_aprobados']:.1f}%"
)
st.subheader("Estadísticas por asignatura")

estadisticas_asignaturas = negocio.obtener_estadisticas_asignaturas(
    datos_filtrados
)

st.dataframe(
    estadisticas_asignaturas,
    width="stretch",
    hide_index=True
)
st.subheader("Rendimiento por alumno")

estadisticas_alumnos = negocio.obtener_estadisticas_alumnos(
    datos_filtrados
)

st.dataframe(
    estadisticas_alumnos,
    use_container_width=True,
    hide_index=True
)
st.subheader("Representación gráfica")

tab1, tab2, tab3 = st.tabs([
    "Notas por asignatura",
    "Evolución de evaluaciones",
    "Distribución de notas"
])
with tab1:

    fig = graficos.grafico_notas_asignaturas(
        estadisticas_asignaturas
    )

    st.pyplot(fig)

    import matplotlib.pyplot as plt
    plt.close(fig)
    
with tab2:
    evolucion = negocio.obtener_evolucion_evaluaciones(
        datos,
        curso,
        asignatura,
        grupo
    )

    if evolucion.is_empty():
        st.info("No hay datos suficientes para mostrar la evolución.")
    else:
        fig = graficos.grafico_evolucion_evaluaciones(
            evolucion
        )

        st.pyplot(fig)

        import matplotlib.pyplot as plt
        plt.close(fig)
        
with tab3:

    fig = graficos.grafico_distribucion_notas(
        datos_filtrados
    )

    st.pyplot(fig)

    import matplotlib.pyplot as plt
    plt.close(fig)