import streamlit as st
import plotly.express as px
from servicios.analisis import calcular_kpis, resumen_por_mes, analisis_regiones

def mostrar(df):
    st.title("Resumen del negocio")
    if df.empty:
        st.warning("No hay ventas para los filtros seleccionados.")
        return
    k = calcular_kpis(df)
    c1,c2,c3 = st.columns(3)
    c1.metric("Facturación", f'{k["facturacion"]:,.2f} €')
    c2.metric("Beneficio", f'{k["beneficio"]:,.2f} €')
    c3.metric("Número de ventas", k["ventas"])
    c4,c5,c6 = st.columns(3)
    c4.metric("Unidades vendidas", k["unidades"])
    c5.metric("Ticket medio", f'{k["ticket_medio"]:,.2f} €')
    c6.metric("Margen medio", f'{k["margen_medio"]:.1f} %')

    mensual = resumen_por_mes(df)
    st.subheader("Evolución mensual")
    if not mensual.empty:
        fig = px.line(mensual, x="mes", y=["facturacion","beneficio"],
                      markers=True, title="Facturación y beneficio por mes")
        st.plotly_chart(fig, use_container_width=True)

    regiones = analisis_regiones(df)
    c1,c2 = st.columns(2)
    with c1:
        st.subheader("Facturación por región")
        st.plotly_chart(px.bar(regiones, x="region", y="facturacion"), use_container_width=True)
    with c2:
        st.subheader("Ventas por categoría")
        categorias = df.groupby("categoria", as_index=False)["importe_neto"].sum()
        st.plotly_chart(px.pie(categorias, names="categoria", values="importe_neto",
                               title="Distribución de facturación"), use_container_width=True)
