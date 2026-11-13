cursos=[{"nombre":"python","duracion":50},
        {"nombre":"java","duracion":30},
        {"nombre":"angular","duracion":40}
        ]

#ordenar la lista por duracion de cursos
#cursos.sort(key=lambda c:c["duracion"])
#print(cursos)
print(sorted(cursos,key=lambda c:c["duracion"]))

#mostrar los nombres de todos los cursos
print(list(map(lambda c:c["nombre"],cursos)))