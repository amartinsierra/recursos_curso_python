import pandas as pd
import datetime
import matplotlib.pyplot as plot
#cargamos un DataFrame con con los datos del fichero
datafr=pd.read_json("contagios.json",encoding="UTF-8")

def menu():
    print("1. Contagios de pais")
    print("2. Contagios posteriores a fecha")
    print("3. País con más contagios")
    print("4. Gráfico contagios por pais")
    print("5.- Salir")
def transformarafecha(texto):
    formato="%Y-%m-%d"
    return datetime.datetime.strptime(texto,formato)
def contagiospais(nombrepais):    
    return datafr.groupby("pais")["contagios"].sum()[nombrepais]
def contagiosposterioresfecha(fecha):
    f=transformarafecha(fecha)
    return datafr.query("fecha>@f")["contagios"].sum()
def paismascontagios():
    return datafr.groupby("pais")["contagios"].sum().sort_values(ascending=False).index[0]
def graficocontagios():
    datafr.groupby("pais")["contagios"].sum().plot(kind="bar")
    plot.show()
opcion=0
#transformamos la columna fecha de texto a tipo fecha
datafr["fecha"]=datafr["fecha"].map(lambda x:transformarafecha(x))
while opcion!="5":
    menu()
    opcion=input("Introduce opción: ")
    if opcion=="1":
        nombre=input("Introduce nombre de país: ")
        print("Total de contagios en ",nombre,": ",contagiospais(nombre))
    elif opcion=="2":
        fecha=input("Introduce fecha (año-mes-dia): ")
        print("Total de contagios posteriores a esa fecha: ",contagiosposterioresfecha(fecha))
    elif opcion=="3":
        print("País con más contagios ",paismascontagios())
    elif opcion=="4":
        graficocontagios()



