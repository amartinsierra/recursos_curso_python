import pandas as pd
df=pd.read_json("alumnos.json")
grupos=df.groupby("curso")
print("Total de alumnos de cada grupo:")
print(grupos["nombre"].count())
print("Nota media por curso")
print(grupos["nota"].mean())