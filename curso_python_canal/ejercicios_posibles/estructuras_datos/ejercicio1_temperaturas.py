resp="s"
temps=[]
while resp=="s":
    tmp=float(input("Introduce temperatura: "))
    if tmp not in temps:
        temps.append(tmp)
    else:
        print("Ese valor ya existe")
    resp=input("¿Desea introducir una nueva temperatura(s/n)?")
media=0
for t in temps:
    media+=t
print("Temperatura media: ",media/len(temps))
print("Temperatura máxima: ",max(temps))
print("Temperatura mínima: ",min(temps))