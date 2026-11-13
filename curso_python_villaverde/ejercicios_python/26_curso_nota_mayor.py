cursos=("Python","Java","Spring")
notas=[(8,3,4,5),(2,4,7,3,6),(7,6,7,3,5)]
#En que curso se ha obtenido la media más alta
def media(tupla):
    suma=0
    for n in tupla:
        suma+=n
    return suma/len(tupla)
posicion=0
media_mayor=0

