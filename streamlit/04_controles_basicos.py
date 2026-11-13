import streamlit as st
nombre = st.text_input("Introduce tu nombre")

st.write("Nombre:", nombre)
edad = st.number_input(
    "Introduce tu edad",
    min_value=0,
    max_value=120,
    value=18
)

st.write("Edad:", edad)
activo = st.checkbox("Alumno activo")

st.write("Activo:", activo)
curso = st.selectbox(
    "Selecciona un curso",
    ["Python", "Java", "Angular", "Spring"]
)

st.write("Curso:", curso)
nivel = st.radio(
    "Nivel",
    ["Básico", "Intermedio", "Avanzado"]
)
if st.button("Saludar"):
    st.success(f"Te llamas {nombre} tienes {edad} años y quieres estudiar {curso} nivel {nivel}")