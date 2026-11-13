#solicita una nota, despues otra, y así sucesivamente hasta introducir un cero
#en ese momento, no pedirá más notas y mostrará la nota media de las introducidas 
#hasta el momento

suma=0
total=0
nota=int(input("Introduce nota"))
while nota>0:
    total=total+1
    suma=suma+nota
    nota=int(input("Introduce nota"))
print("Nota media: ",suma/total)  