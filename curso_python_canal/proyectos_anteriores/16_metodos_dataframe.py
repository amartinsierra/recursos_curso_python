import pandas as pd
df=pd.read_json("alumnos.json")
#calculos estadísticos del curso solicitado al usuario
curso=input("Introduce curso: ")
dfiltrado=df.query("curso==@curso")
print("Nota media: ",dfiltrado["nota"].mean())
print("Nota más alta: ",dfiltrado["nota"].max())
print("Nota más baja: ",dfiltrado["nota"].min())