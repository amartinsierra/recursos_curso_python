#se pide la introducción de un número y después se calcula la
#suma de todos los números entre 1 y ese número
num=input("Dime el límite")
num=int(num)
suma=0
for n in range(1,num+1):
    suma=suma+n
print("Suma final ",suma)