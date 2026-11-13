import streamlit as st

st.title("Ventas mensuales")
"""
meses = ["Enero", "Febrero", "Marzo", "Abril"]

ventas = [1200, 1800, 1500, 2200]

datos = dict(zip(meses, ventas))

st.bar_chart(datos)
"""
ventas = {
    "Enero": 1200,
    "Febrero": 1800,
    "Marzo": 1500,
    "Abril": 2200
}

st.title("Ventas mensuales")

st.bar_chart(ventas)