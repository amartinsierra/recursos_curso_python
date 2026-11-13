#lista de reproducción
lista_reproduccion=[
    {"titulo":"canción inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
]
#Solicita al usuario del programa
#la introducción de una nueva canción (titulo, duracion y valoracion)
titulo=input("Título de la canción ")
duracion=float(input("Duración de la canción "))
valoracion=int(input("Valoración de la canción "))
"""
cancion={}
cancion["titulo"]=titulo
cancion["duracion"]=duracion
cancion["valoracion"]=valoracion
"""
#alternativa a lo anterior:
cancion={
    "titulo":titulo,
    "duracion":duracion,
    "valoracion":valoracion
}

lista_reproduccion.append(cancion)#añade canción a la lista
#mostrar los títulos de todas las canciones
for c in lista_reproduccion:
    print(c["titulo"])

#mostrar la valoracion media
suma=0
for c in lista_reproduccion:
    suma=suma+c["valoracion"]
print("La valoración media es: ",suma/len(lista_reproduccion))

#mostrar el titulo de la canción con mas duración
duracion_mayor=0
titulo_mayor=""
for c in lista_reproduccion:
    if c["duracion"]>duracion_mayor:
        duracion_mayor=c["duracion"]
        titulo_mayor=c["titulo"]
        
print("La canción más larga es: ",titulo_mayor)