import streamlit as st
from servicios.analisis import detectar_anomalias_iqr

def mostrar(df):
    st.title("Detección de anomalías")
    if df.empty:
        st.info("No hay datos.")
        return
    columna = st.selectbox("Variable que se analizará", ["importe_neto","beneficio","unidades"])
    anomalias, inferior, superior = detectar_anomalias_iqr(df, columna)
    c1,c2,c3 = st.columns(3)
    c1.metric("Límite inferior", f"{inferior:,.2f}")
    c2.metric("Límite superior", f"{superior:,.2f}")
    c3.metric("Anomalías detectadas", len(anomalias))
    st.caption("Método del rango intercuartílico: Q1 − 1,5 × IQR y Q3 + 1,5 × IQR.")
    if anomalias.empty:
        st.success("No se han detectado valores atípicos.")
    else:
        st.dataframe(anomalias[["id_venta","fecha","producto","region",columna]],
                     use_container_width=True, hide_index=True)
    st.warning("Una anomalía estadística no implica necesariamente un error. No se eliminan automáticamente.")
