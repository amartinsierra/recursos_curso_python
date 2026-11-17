import polars as pl

datos = [
    {"nombre": "Ana", "edad": 25, "salario": 25000},
    {"nombre": "Luis", "edad": 32, "salario": 32000},
    {"nombre": "Marta", "edad": 28, "salario": 28000},
    {"nombre": "Pedro", "edad": 41, "salario": 41000}
]
df = pl.DataFrame(datos)
#convertir dataframe a diccionario:
print(df.to_dicts())
#filtrar filas
print(df.filter(pl.col("edad")>30).to_dicts())

#ordenar
print(df.sort("salario").to_dicts())
#realiza cálculos en columnas y devuelve 
# una dataframe de una fila con los valores calculados
resultado = df.select(
    pl.col("edad").mean().alias("edad_media"),
    pl.col("salario").mean().alias("salario_medio")
)
print(resultado.to_dicts())

#recorrido como diccionarios:
for fila in df.iter_rows(named=True):
    print(fila)
    
#nombre de persona con más salario:
print(df.sort("salario",descending=True).row(0)[0])    

print(df["edad"].min())
print(df["salario"].mean())