edades_alumnos=[17,29,19,22,16]
#cual es la media de edad de los alumnos del curso
suma=0
for n in edades_alumnos:
    suma+=n
media=suma/len(edades_alumnos)
print("La media de edad es ",media)