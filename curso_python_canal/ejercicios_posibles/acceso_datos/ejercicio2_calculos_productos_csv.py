import csv
productocaro=""
preciomax=0
productomenosunidades=""
unidadesmin=-1
preciomedio=0
f=open("productos.csv","r")
prods=csv.DictReader(f,delimiter=";")
for p in prods:
    precio=float(p["preciounitario"])
    unidades=int(p["unidades"])
    if precio>preciomax:
        preciomax=precio
        productocaro=p["producto"]
    if unidades<unidadesmin or unidadesmin==-1:
        unidadesmin=unidades
        productomenosunidades=p["producto"]
    preciomedio+=precio
print("Nombre del producto más caro: ",productocaro)
print("Nombre del producto con menos unidades: ",productomenosunidades)
print("Precio medio: ",preciomedio/prods.line_num)