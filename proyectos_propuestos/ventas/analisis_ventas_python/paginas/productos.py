import streamlit as st
import plotly.express as px
from servicios.analisis import ranking_productos

def mostrar(df):
    st.title("Análisis de productos")
    if df.empty:
        st.info("No hay datos.")
        return
    categorias = ["Todas"] + sorted(df["categoria"].dropna().unique().tolist())
    categoria = st.selectbox("Categoría", categorias)
    datos = df if categoria == "Todas" else df[df["categoria"] == categoria]
    ranking = ranking_productos(datos)
    c1,c2 = st.columns(2)
    with c1:
        st.subheader("10 productos con mayor facturación")
        st.dataframe(ranking.nlargest(10,"facturacion"), use_container_width=True, hide_index=True)
    with c2:
        st.subheader("10 productos con mayor beneficio")
        st.dataframe(ranking.nlargest(10,"beneficio"), use_container_width=True, hide_index=True)
    st.subheader("Unidades vendidas y beneficio")
    fig = px.scatter(ranking, x="unidades", y="beneficio", color="categoria",
                     hover_name="producto", size="facturacion")
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Productos con menor margen")
    st.dataframe(ranking.nsmallest(10,"margen_medio"), use_container_width=True, hide_index=True)
