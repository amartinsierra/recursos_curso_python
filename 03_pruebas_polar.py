import polars as pl

datos = [
    {"nombre": "Ana", "edad": 25, "salario": 25000},
    {"nombre": "Luis", "edad": 32, "salario": 32000},
    {"nombre": "Marta", "edad": 28, "salario": 28000},
    {"nombre": "Pedro", "edad": 41, "salario": 41000}
]

df = pl.DataFrame(datos)

print(df["nombre"]) #como serie
print(df["nombre"].to_list()) #como lista de datos
print(df.row(0)) #como tupla
print(df.row(0,named=True)) #como diccionario
resultado = df.filter(
    (pl.col("edad") > 25) &
    (pl.col("salario") > 30000)
)
print(resultado)
resultado = df.select(
    pl.col("edad").mean().alias("edad_media"),
    pl.col("salario").mean().alias("salario_medio")
)
print(resultado)



datos = [
    {"nombre": "Ana", "departamento": "IT", "salario": 30000},
    {"nombre": "Luis", "departamento": "IT", "salario": 35000},
    {"nombre": "Marta", "departamento": "RRHH", "salario": 28000},
    {"nombre": "Pedro", "departamento": "RRHH", "salario": 32000}
]

df = pl.DataFrame(datos)

resultado = df.group_by("departamento").agg(
    pl.col("salario").mean().alias("salario_medio"),
    pl.col("salario").max().alias("salario_maximo"),
    pl.len().alias("numero_empleados")
)

print(resultado)