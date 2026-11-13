import Notas_Service,streamlit as st
notas_service=Notas_Service.Notas_Service()
nota=st.text_input("Introduce nota")
if st.button("Guardar"):
    notas_service.nueva_nota(nota)
    st.toast("Nota guardada")
if st.button("Mostrar extremas"):
    st.toast(f"Nota más alta: {notas_service.nota_alta()}. Nota más baja:{notas_service.nota_baja()}")
if st.button("Aprobados"):
    st.toast(f"Total de aprobados: {notas_service.aprobados()}")
if st.button("Media"):
    st.toast(f"Nota media: {notas_service.media()}")
if st.button("Mostrar todas"):
    st.table(notas_service.mostrar_notas())
