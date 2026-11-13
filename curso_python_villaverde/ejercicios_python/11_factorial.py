#se pide un número y se calcula el factorial de ese número
num=int(input("Introduce el límite: "))
multi=1
for n in range(1,num+1):
    multi=multi*n
print("El factorial es: ",multi)