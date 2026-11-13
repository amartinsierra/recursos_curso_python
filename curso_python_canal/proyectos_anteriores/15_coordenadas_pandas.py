#El ejercicio de las coordenadas utilizando pandas
import math,pandas
def distancia(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return math.hypot(x2-x1,y2-y1)
posx=int(input("Introduce tu posición x: "))
posy=int(input("Introduce tu posición y: "))
min_aux=1000; #distancia mínima encontrada
tupla_aux=(10000,10000); #coordenadas más cercanas al punto
df=pandas.read_csv("coordenadas.csv")
for k,n in df.iterrows():
    dist=distancia((posx,posy),(int(n["x"]),int(n["y"])))
    if dist<min_aux:
        min_aux=dist
        tupla_aux=(int(n["x"]),int(n["y"]))
print("El punto más cercano a tu posición es: ",tupla_aux)