#Hacer un programa que solicite la introducción de 10 nota
#después, nos mostrará la nota media
suma=0
for n in range(1,11):
    nota=float(input("Introduce nota (entre 0 y 10): "))
    while nota<0 or nota>10:
        print("Nota no válida, vuelva a introducirla")
        nota=float(input("Introduce nota (entre 0 y 10): "))
    suma=suma+nota
print("La nota media es ",suma/10)