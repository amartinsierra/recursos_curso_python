import math,csv
#función para calcular la distancia entre dos puntos
def distancia(punto1,punto2):
    return math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1])
#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista. Cada vez que solicitamos coordenadas
#preguntamos si quiere introducir nuevas coordenadas. En caso afirmativo, se solicitan de nuevo
#si responde que no, finaliza el programa
coordenadas=[]
f=open("coordenadas.csv","r")
coordenadas=list(map(lambda d:(int(d["x"]),int(d["y"])),list(csv.DictReader(f))))
print(coordenadas)
#Pedimos al usuario su posición y le mostraremos las coordenadas del punto 
#más cercano a su posición
pos_x=int(input("Tu posición x: "))
pos_y=int(input("Tu posición y: "))
pos_user=(pos_x,pos_y)
distancia_min=10000
pos_encontrada=None
for c in coordenadas:
    #para coordenada calculamos la distancia entre la coordenada y pos de usuario
    #si la distancia es inferior a distancia_min, actualizamos esta variable y también
    #la de posición encontrada
    d=distancia(c,pos_user)
    if d<distancia_min:
        distancia_min=d
        pos_encontrada=c

print("El punto más cercano a tu posición es ",pos_encontrada)



