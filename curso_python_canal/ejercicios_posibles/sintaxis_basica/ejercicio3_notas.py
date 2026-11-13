media=0
aprobados=0
alta=0
baja=10
for i in range(1,11):
    nota=int(input("Introduce una nota entre 0 y 10"))
    media+=nota
    if nota>=5:
        aprobados+=1
    if nota>alta:
        alta=nota
    if nota<baja:
        baja=nota
print("La nota media es: ",media/10)
print("Número de aprobados: ",aprobados)
print("La nota más baja es: ",baja)
print("La nota más alta es: ",alta)
