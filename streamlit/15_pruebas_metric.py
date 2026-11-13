import streamlit as st

col1, col2, col3 = st.columns(3)

col1.metric("Ventas", "12.500 €", "+15%")
col2.metric("Clientes", 350, "+25")
col3.metric("Productos", 120, "-5")