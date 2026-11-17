import pandas as pd
df=pd.read_csv("empresa.csv",encoding="UTF-8")
#print(df.loc[0].to_dict())
#print(df.loc[1].to_list())

""" grupo=df.groupby("departamento",as_index=False).agg(   #sin as_index=False no sale el departamento
    salario_medio=("salario","mean"),
    edad_maxima=("edad","max"))
print(grupo.to_dict(orient="records")) """
"""
for k,v in df.iterrows():
    print (k)
    print("-",v.to_dict()) #{'empleado': 'Raquel', 'edad': 28, 'salario': 1100, 'departamento': 'ventas'}
for v in df.values:
    print(v) #['Marcos' 39 1300 'informática']

for departamento, grupo in df.groupby("departamento",as_index=False):
    print(departamento)
    print(grupo.to_dict(orient="records"))
    """
print(df.groupby("departamento",as_index=False).get_group("informática"))
print(df["departamento"].to_list())