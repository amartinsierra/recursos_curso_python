import polars as pl
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

print(resultado.to_dicts())

datos = [
    {"nombre": "Ana", "curso": "Java", "nota": 7},
    {"nombre": "Luis", "curso": "Python", "nota": 3},
    {"nombre": "Marta", "curso": "Java", "nota": 2},
    {"nombre": "Pedro", "curso": "C++", "nota": 6}
]

df=pl.DataFrame(datos)
print(df.select(pl.col("nota").mean().alias("nota media"),
          pl.col("nota")
          .filter(pl.col("nota") >= 5)
          .count()
          .alias("aprobados")
          )
)