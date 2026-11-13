#vamos a crear una lista de objetos para un videojuego
#un ejemplo de objeto sería:
objeto = {
    "nombre": "Espada",
    "ataque": 10,
    "peso": 5
}

#solicitar la introducción de tres objetos y guardarlos en una lista
inventario=[]
for n in range(1,4):
    nombre=input("Introduce nombre ")
    ataque=input("Introduce ataque ")
    peso=input("Introduce peso ")
    objeto={
    "nombre": nombre,
    "ataque": int(ataque),
    "peso": int(peso) 
    }
    inventario.append(objeto)
print(inventario)
print("-------------------------")

#pedir la introducción del nombre de un objeto, a continuación
#el nuevo peso a asignar y lo actualizará
nombre=input("Dame el nombre del objeto: ")
nuevo_peso=int(input("Dame su nuevo peso: "))
for o in inventario:
    if o["nombre"]==nombre:
        o["peso"]=nuevo_peso
print(inventario)
print("-------------------------")

def fuerza(peso,ataque):
    return ataque*2+peso*1.5

#mostrar objeto con más fuerza
mayor_fuerza=0
nombre_mayor=""
for o in inventario:
    #si la fuerza del objeto es mayor que mayor_fuerza, se actualiza la variable
    f=fuerza(o["peso"],o["ataque"])
    if f>mayor_fuerza:
        mayor_fuerza=f
        nombre_mayor=o["nombre"]
print("El objeto con más fuerza es: ",nombre_mayor)

