#solicitar la introducción de numeros, uno a uno
#y los guardamos en una lista. Después de pedir un número,
#pregunta si quiere introducir otro, y así hasta que diga que no
lista=[]
resp="s"
while resp=="s" or resp=="S":
    num=int(input("Escribe un número "))
    lista.append(num)
    resp=input("¿Desea introducir otro número(s/n)? ")
print(lista)