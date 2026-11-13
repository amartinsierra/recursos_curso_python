numeros=[9,2,-1,7,-4,11,32,-7,8]
#calcula la suma de todos los números positivos de la lista
suma=0
for n in numeros:
    if n>0:
        suma+=n
print("Suma de positivos: ",suma)