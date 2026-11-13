import streamlit as st
import pandas as pd
from servicios.carga_datos import cargar_datos
from servicios.limpieza import limpiar_datos
from paginas import resumen, productos, clientes, anomalias

st.set_page_config(page_title="Analítica de ventas", page_icon="📊", layout="wide")

@st.cache_data
def obtener_datos():
    bruto = cargar_datos()
    return limpiar_datos(bruto)

try:
    df, informe = obtener_datos()
except Exception as e:
    st.error(f"No se pudieron cargar los datos: {e}")
    st.stop()

st.sidebar.title("Analítica de ventas")
st.sidebar.caption("Panel de inteligencia de negocio")
pagina = st.sidebar.radio("Secciones", [
    "Resumen", "Productos", "Clientes y regiones", "Anomalías", "Calidad de datos"
])

st.sidebar.divider()
st.sidebar.subheader("Filtros")
fecha_min = df["fecha"].min().date()
fecha_max = df["fecha"].max().date()
rango = st.sidebar.date_input("Periodo", value=(fecha_min, fecha_max),
                              min_value=fecha_min, max_value=fecha_max)
if isinstance(rango, (tuple, list)) and len(rango) == 2:
    fecha_inicio, fecha_fin = rango
else:
    fecha_inicio, fecha_fin = fecha_min, fecha_max

def opciones(columna):
    return ["Todas"] + sorted(df[columna].dropna().unique().tolist())

categoria = st.sidebar.selectbox("Categoría", opciones("categoria"))
region = st.sidebar.selectbox("Región", opciones("region"))
vendedor = st.sidebar.selectbox("Vendedor", opciones("vendedor"))
metodo = st.sidebar.selectbox("Método de pago", opciones("metodo_pago"))

filtrado = df[df["fecha"].between(pd.Timestamp(fecha_inicio), pd.Timestamp(fecha_fin))]
for columna, valor in [("categoria",categoria),("region",region),
                       ("vendedor",vendedor),("metodo_pago",metodo)]:
    if valor != "Todas":
        filtrado = filtrado[filtrado[columna] == valor]

if pagina == "Resumen":
    resumen.mostrar(filtrado)
elif pagina == "Productos":
    productos.mostrar(filtrado)
elif pagina == "Clientes y regiones":
    clientes.mostrar(filtrado)
elif pagina == "Anomalías":
    anomalias.mostrar(filtrado)
else:
    st.title("Calidad de los datos")
    st.write("Informe de limpieza aplicado al CSV original.")
    st.dataframe(pd.DataFrame(
        [{"Indicador": k, "Valor": v} for k,v in informe.items()]
    ), use_container_width=True, hide_index=True)
    st.subheader("Vista previa de los datos limpios")
    st.dataframe(df, use_container_width=True, hide_index=True)

st.sidebar.caption(f"Registros analizados: {len(filtrado)} de {len(df)}")
