#Se pide el nombre de un curso
#y se muestran los nombres de todos los alumnos que están en ese curso
import json
f=open("alumnos.json","r")
curso=input("Introduce nombre del curso: ")
for al in json.load(f):
    if al["curso"]==curso:
        print(al["nombre"],"-",al["nota"])