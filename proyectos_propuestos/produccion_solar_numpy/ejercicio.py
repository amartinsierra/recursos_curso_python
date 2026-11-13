import numpy as np

produccion = np.array([
    1250, 1380, 980, 1450, 1520, 1100, 1600
])

dias = np.array([
    "Lunes", "Martes", "Miércoles", "Jueves",
    "Viernes", "Sábado", "Domingo"
])

# 1. Mostrar producción de cada día
for dia, energia in zip(dias, produccion):
    print(f"{dia}: {energia} kWh")

# 2. Producción total semanal
total = np.sum(produccion)
print(f"\nProducción total: {total} kWh")

# 3. Producción media diaria
media = np.mean(produccion)
print(f"Producción media: {media:.2f} kWh")

# 4. Día con mayor y menor producción
indice_max = np.argmax(produccion)
indice_min = np.argmin(produccion)

print(f"Mayor producción: {dias[indice_max]} ({produccion[indice_max]} kWh)")
print(f"Menor producción: {dias[indice_min]} ({produccion[indice_min]} kWh)")

# 5. Días con producción superior a la media
dias_superiores = dias[produccion > media]

print("\nDías con producción superior a la media:")
print(dias_superiores)

# 6. Porcentaje de producción de cada día
porcentajes = produccion / total * 100

print("\nPorcentaje de producción diaria:")
for dia, porcentaje in zip(dias, porcentajes):
    print(f"{dia}: {porcentaje:.2f}%")

# 7. Simular incremento del 8 %
nueva_produccion = produccion * 1.08

print("\nProducción con mejora del 8 %:")
print(nueva_produccion)

# 8. Ampliación: días con producción baja
dias_baja_produccion = dias[produccion < media * 0.8]

print("\nDías con producción un 20 % inferior a la media:")
print(dias_baja_produccion)