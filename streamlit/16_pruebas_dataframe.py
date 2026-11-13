import streamlit as st

datos = [
    {"producto": "Portátil", "precio": 850},
    {"producto": "Monitor", "precio": 250},
    {"producto": "Teclado", "precio": 45}
]

st.dataframe(datos)