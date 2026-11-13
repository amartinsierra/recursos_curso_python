import pandas as pd
df=pd.read_csv("coordenadas.csv")
print(df.iloc[0]["x"]) #coordena x de la primera fila
#mostrar los valores de la coordenada x de todas las filas
for k,v in df.iterrows():
    print(v["x"])