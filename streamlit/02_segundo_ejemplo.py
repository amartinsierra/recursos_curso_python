import streamlit as st

st.title("Título principal")
st.header("Encabezado")
st.subheader("Subencabezado")
st.text("Texto normal")
st.write({"nombre":"Paco","edad":40})
#con un arterisco cursiva, con dos negrita y con tres negrita y cursiva
st.markdown("**Texto en negrita**",text_alignment="right")
st.caption("Texto secundario")