#se solicita el presupuesto al usuario. A partir de ahí, 
#le muestra las viviendas a las que puede optar
import csv
f=open("houses.csv","r")
presupuesto=int(input("Dime tu presupuesto: "))
#print(list(filter(lambda h:int(h["price"])<=presupuesto,list(csv.DictReader(f)))))
#con programación convencional
next(f)
for h in csv.reader(f):
    if int(h[4])<=presupuesto:
        print("Tamaño: ",h[0]," habitaciones: ",h[1]," antiguedad: ",h[2])

