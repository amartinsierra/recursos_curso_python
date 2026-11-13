import streamlit as st

alumnos = ["Juan", "Ana", "Pedro"]

st.write(alumnos)
alumno = {
    "id": 1,
    "nombre": "Juan",
    "edad": 25,
    "curso": "Python"
}

st.write(alumno)
aula = [
    {"id": 1, "nombre": "Juan", "edad": 25},
    {"id": 2, "nombre": "Ana", "edad": 30},
    {"id": 3, "nombre": "Pedro", "edad": 22}
]

st.table(aula)