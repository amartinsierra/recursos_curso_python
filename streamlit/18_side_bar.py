import streamlit as st
st.sidebar.title("Menú")

opcion = st.sidebar.selectbox(
    "Selecciona una opción",
    ["Productos", "Clientes", "Ventas"]
)

st.title("Aplicación de gestión")

st.write("Has seleccionado:", opcion)