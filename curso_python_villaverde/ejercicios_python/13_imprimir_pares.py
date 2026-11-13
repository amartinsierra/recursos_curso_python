#se pide la introducción de dos números y el programa nos muestra
#los números pares comprendidos entre los dos números
num1=int(input("Introduce el número pequeño "))
num2=int(input("Introduce el número mayor "))
menor=min(num1,num2)
mayor=max(num1,num2)
for n in range(menor,mayor+1):
    if n%2==0:
        print(n)