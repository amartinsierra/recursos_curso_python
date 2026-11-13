#definir funciones

def repetido(lista, numero):
    rep=False
    for n in lista:
        if numero==n:
            rep=True
    return rep

#solicitar la introducción de numeros, uno a uno
#y los guardamos en una lista, NO debe permitir números repetidos. Después de pedir un número,
#pregunta si quiere introducir otro, y así hasta que diga que no
lista=[]
resp="s"
while resp=="s" or resp=="S":
    num=int(input("Escribe un número "))
    #hay que modificar esto, para que solo añada el numero
    #en caso de que no esté    
    if repetido(lista,num)==False:
        lista.append(num)
    else:
        print("Número, repetido, no lo añado!")
    resp=input("¿Desea introducir otro número(s/n)? ")
print(lista)

