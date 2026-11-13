import streamlit as st
import time
mensaje=st.success("Operación realizada correctamente")
st.error("Se ha producido un error")
st.warning("Atención")
st.info("Información adicional")
time.sleep(3)
mensaje.empty() #desaparece a los tres segundos