import matplotlib.pyplot as plt

""" meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
consumo = [120, 150, 135, 180, 160]

plt.bar(meses, consumo)

plt.title("Consumo eléctrico mensual")
plt.xlabel("Mes")
plt.ylabel("Consumo (kWh)")

plt.show()
edificios = ["Oficinas", "Almacén", "Fábrica", "Tienda"]
consumo = [350, 220, 580, 190]

plt.pie(
    consumo,
    labels=edificios,
    autopct="%1.1f%%"
)

plt.title("Distribución del consumo")

plt.show()
 """
import matplotlib.pyplot as plt

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]

instalacion_a = [120, 150, 135, 180, 160]
instalacion_b = [100, 130, 145, 155, 170]

plt.plot(meses, instalacion_a, marker="o", label="Instalación A")
plt.plot(meses, instalacion_b, marker="s", label="Instalación B")

plt.title("Comparativa de consumo")
plt.xlabel("Mes")
plt.ylabel("Consumo (kWh)")

plt.legend()
plt.grid(True)

plt.show()