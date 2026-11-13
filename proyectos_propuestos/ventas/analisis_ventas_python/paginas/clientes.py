import streamlit as st
import plotly.express as px
from servicios.analisis import ranking_clientes, analisis_regiones

def mostrar(df):
    st.title("Clientes y regiones")
    if df.empty:
        st.info("No hay datos.")
        return
    clientes = ranking_clientes(df)
    c1,c2 = st.columns(2)
    with c1:
        st.subheader("10 clientes con mayor compra")
        st.dataframe(clientes.nlargest(10,"importe_total"), use_container_width=True, hide_index=True)
    with c2:
        st.subheader("10 clientes que generan más beneficio")
        st.dataframe(clientes.nlargest(10,"beneficio"), use_container_width=True, hide_index=True)
    st.subheader("Análisis geográfico")
    regiones = analisis_regiones(df)
    st.dataframe(regiones, use_container_width=True, hide_index=True)
    st.plotly_chart(px.bar(regiones, x="region", y=["facturacion","beneficio"],
                           barmode="group", title="Facturación y beneficio por región"),
                    use_container_width=True)
