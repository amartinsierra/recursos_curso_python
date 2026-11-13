palabras=["casa","diccionario","telefono","as","pruebas"]
#mostrar la palabra más larga
palabra_mayor=""
for p in palabras:
    if len(p)>len(palabra_mayor): #comparamos longitudes
        palabra_mayor=p
print("La palabra más larga es ",palabra_mayor)