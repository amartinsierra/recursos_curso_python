import datetime
fechas="03/10/2023,1/06/2021,10/10/2020,4/5/2024"
valores=fechas.split(",")
fmenor=datetime.datetime.strptime(valores[0],"%d/%m/%Y")
for f in valores:
    fecha=datetime.datetime.strptime(f,"%d/%m/%Y")
    if fecha<fmenor:
        fmenor=fecha
print("La fecha más antigua es: ",fmenor)