import streamlit as st
with st.container(border=True):
    st.title("Datos del alumno")
    st.text_input("Nombre")
    st.text_input("Curso")
col1, col2 = st.columns(2)

with col1:
    st.write("Contenido de la izquierda1")
    st.write("Contenido de la izquierda2")
    st.write("Contenido de la izquierda3")

with col2:
    st.write("Contenido de la derecha1")
    st.write("Contenido de la derecha2")
    st.write("Contenido de la derecha3")