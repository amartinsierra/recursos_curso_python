import csv
import pandas as pd
df=pd.read_csv("productos.csv",encoding="UTF-8",delimiter=";")
pospreciomax=df["preciounitario"].idxmax()
posunidadesmin=df["unidades"].idxmin()
print("Nombre del producto más caro: ",df["producto"][pospreciomax])
print("Nombre del producto con menos unidades: ",df["producto"][posunidadesmin])
print("Precio medio: ",df["preciounitario"].mean())
