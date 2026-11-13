lista_notas=[6,2,5,4,8,7]
#calcular la nota media
suma=0
for n in lista_notas:
    suma=suma+n
print("La nota media es ",suma/len(lista_notas))

#mostrar la nota más alta y la más baja
max=0
min=10
for n in lista_notas:
    if n<min:
        min=n
    if n>max:
        max=n
print("El número más alto es: ",max)
print("El número más bajo es: ",min)