#Teniendo en cuenta, que alevin es 10 años y benjamin es 16.
#Pide la edad al usuario y dile a que grupo pertenece(al más cercano serún su edad). La edad
#debe estar entre 10 y 16.
alevin=10
benjamin=16
edad=int(input("Dime tu edad: "))
if edad<alevin or edad>benjamin:
    print("Edad no válida")
else:
    distancia_benjamin=benjamin-edad
    distancia_alevin=edad-alevin
    if(distancia_benjamin<distancia_alevin):
        print("Perteneces al grupo benjamín")
    else:
        print("Perteneces al grupo alevín")
