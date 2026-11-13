import streamlit as st
if "alumnos" not in st.session_state:
    alumnos=[] 
    st.session_state.alumnos=alumnos
else:
    alumnos=st.session_state.alumnos
st.title("Gestión de alumnos")

tab1, tab2 = st.tabs(
    ["Alta", "Consulta"]
)
with tab1:
    nombre=st.text_input("Introduce nombre: ")
    curso=st.text_input("Introduce curso: ")
    nota=st.number_input("Introduce nota: ",min_value=0,max_value=10)
    if st.button("Guardar"):
        alumnos.append({"nombre":nombre,"curso":curso,"nota":nota})
with tab2:
    curso_sel=st.selectbox("Selecciones curso",list(set([c["curso"] for c in alumnos])))
    st.table([alumno for alumno in alumnos if alumno["curso"]==curso_sel])