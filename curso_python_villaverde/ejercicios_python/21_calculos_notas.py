notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]
#indica cuantos alumnos han aprobado
contar=0
for n in notas_alumnos:
    if n>=5:
        contar=contar+1
print("El total de aprobados es ",contar)

#indica la nota más alta
mayor=0
for n in notas_alumnos:
    if n>mayor:
        mayor=n  #actualizamos con nuevo máximo
print("La nota más alta es ",mayor)
        
#indica la nota más alta versión reducida
print("La nota más alta es ",max(notas_alumnos))
#indica la nota más baja
print("La nota más baja es ",min(notas_alumnos))