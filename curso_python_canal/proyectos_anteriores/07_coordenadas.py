import math
#realizar un programa, que solicite las coordenadas de un punto y las guarde
#en una lista. Después, preguntará si quiere guardar nuevas coordenadas
#y, en caso afirmativo, solicitará nuevas coordenadas. Así sucesivamente, hasta
#que responda que no. En ese momento imprime la lista de coordenadas
#[(1,2),(5,2),(9,2)]


coordenadas=[]
respuesta="S"
while respuesta=="S":
    x=input("valor de x: ")
    y=input("valor de y: ")
    tupla=(int(x),int(y))
    coordenadas.append(tupla)
    respuesta=input("¿Desea introducir nuevas coordenadas? (S/N)")
print(coordenadas)
#segunda parte: Se solicita la introducción de un punto de localización
#A continuación, el programa nos mostrará la coordenada más cercana al punto de localización
#Función que calcula la distancia entre dos puntos
def distancia(p1,p2):
    #x1=p1[0]
    #y1=p1[1]
    #x2=p2[0]
    #y2=p2[1]
    x1,y1=p1
    x2,y2=p2
   # return math.sqrt((x2-x1)**2+(y2-y1)**2)
    return math.hypot(x2-x1,y2-y1)

posx=int(input("Introduce tu posición x"))
posy=int(input("Introduce tu posición y"))

min_aux=1000; #distancia mínima encontrada
tupla_aux=coordenadas[0]; #coordenadas más cercanas al punto
#recorremos las coordenadas y comparamos las distancias con el mínimo
#si encontramos un nuevo mínimo, actualizamos las variables auxiliares
#con sus correspondientes valores
for c in coordenadas:
    dist=distancia(c,(posx,posy))
    if dist<min_aux:
        min_aux=dist
        tupla_aux=c
print("Las coordenas más cercanas a tu posición son: ",tupla_aux)
