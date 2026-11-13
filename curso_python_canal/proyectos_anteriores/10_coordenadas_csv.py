import math,csv
def distancia(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.hypot(x2-x1,y2-y1)
posx=int(input("Introduce tu posición x: "))
posy=int(input("Introduce tu posición y: "))
min_aux=1000; #distancia mínima encontrada
tupla_aux=(10000,10000); #coordenadas más cercanas al punto
f=open("coordenadas.csv","r")

for coord in csv.reader(f,delimiter=","):
    print(coord)
    dist=distancia((posx,posy),(int(coord[0]),int(coord[1])))
    if dist<min_aux:
        min_aux=dist
        tupla_aux=tuple(coord)
print("El punto más cercano a tu posición es: ",tupla_aux)