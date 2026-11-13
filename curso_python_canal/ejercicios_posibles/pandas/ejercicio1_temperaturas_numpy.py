import csv
import numpy as np
f=open("temperaturas.csv","r")
datos=list(csv.reader(f))
tabla=np.array(datos)
tabla=tabla.astype(np.float64)
print("Temperatura máxima total: ",tabla.max())
print("Temperatura mínima total: ",tabla.min())
print("Temperatura máxima de cada ciudad: ", tabla.mean(axis=1))
print("Temperatura media global: ", tabla.mean())
