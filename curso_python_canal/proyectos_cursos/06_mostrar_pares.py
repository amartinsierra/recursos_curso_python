#Realiza un programa que solicite la introducción de un número
#después, muestra todos los pares entre 1 y ese número
num=int(input("Introduce el número"))
for n in range(1,num+1):
    if n%2==0:
        print(n, " es par")