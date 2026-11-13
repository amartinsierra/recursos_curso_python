import streamlit as st

st.title("Alta de alumnos")

with st.form("formulario_alumno"):

    nombre = st.text_input("Nombre")

    edad = st.number_input("Edad", min_value=18)

    curso = st.selectbox(
        "Curso",
        ["Python", "Java", "Angular"]
    )

    enviado = st.form_submit_button("Guardar")

    if enviado:

        st.write("Alumno:", nombre)
        st.write("Edad:", edad)
        st.write("Curso:", curso)