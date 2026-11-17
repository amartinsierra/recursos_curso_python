import matplotlib.pyplot as plt
import streamlit as st

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
consumo = [120, 150, 135, 180, 160]

""" plt.bar(meses, consumo)

plt.title("Consumo eléctrico mensual")
plt.xlabel("Mes")
plt.ylabel("Consumo (kWh)")
st.pyplot(plt) """
edades = [
    18, 19, 20, 21, 22,
    23, 24, 25, 25, 26,
    27, 28, 29, 30, 31,
    32, 35, 38, 42, 45
]
plt.title("Distribución de edades")
plt.xlabel("Edades")
plt.ylabel("Personas")
plt.hist(edades,bins=8,edgecolor="black")
st.pyplot(plt)