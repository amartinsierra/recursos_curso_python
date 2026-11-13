import json
import datetime
def contagiospais(nombrepais):    
    f=open("contagios.json","r",encoding="UTF-8")
    #devuelve una lista de diccionarios
    datos=json.load(f)
    contagios=0
    #recorre cada objeto JSON de la lista y suma los
    #contagios del pais recibido como parámetro
    for item in datos:
        if item["pais"]==nombrepais:
            contagios+=item["contagios"]
    f.close()
    return contagios
def contagiosposterioresfecha(fecha):
    f=open("contagios.json","r",encoding="UTF-8")
    #devuelve una lista de diccionarios
    datos=json.load(f)
    contagios=0
    #recorre cada objeto JSON de la lista y suma los
    #contagios cuyas fechas sean posteriores a la recibida
    for item in datos:
        if transformarafecha(item["fecha"])>transformarafecha(fecha):
            contagios+=item["contagios"]
    f.close()
    return contagios
def paismascontagios():
    f=open("contagios.json","r",encoding="UTF-8")
    #devuelve una lista de diccionarios
    datos=json.load(f)
    #inicializa el resultado al nombre del primer pais
    nombrepais=datos[0]["pais"]
    #recorre cada objeto JSON de la lista y si encuentra un pais
    #cuyos contagios sean superiores a los del pais registrado, actualiza
    #el resultado con el nombre de ese pais
    for item in datos:
        if contagiospais(item["pais"])>contagiospais(nombrepais):
            nombrepais=item["pais"]
    f.close()
    return nombrepais
def transformarafecha(texto):
    formato="%Y-%m-%d"
    return datetime.datetime.strptime(texto,formato)

opcion=0
while opcion!=4:
    print("1. Contagios de pais")
    print("2. Contagios posteriores a fecha")
    print("3. País con más contagios")
    print("4.- Salir")
    opcion=int(input("Introduce opción: "))
    if opcion==1:
        nombre=input("Introduce nombre de país: ")
        print("Total de contagios en ",nombre,": ",contagiospais(nombre))
    elif opcion==2:
        fecha=input("Introduce fecha (año-mes-dia): ")
        print("Total de contagios posteriores a esa fecha: ",contagiosposterioresfecha(fecha))
    elif opcion==3:
        print("País con más contagios ",paismascontagios())