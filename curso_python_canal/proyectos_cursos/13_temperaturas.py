#realizar un programa que solicite los nombres y temperaturas de cinco ciudades
#después nos muestra la temperatura media total y el nombre 
#de la ciudad más fria
ciudades={}
#devuelve True si la ciudad esta en el diccionario
def ciudad_repetida(ciudad):
    return ciudad in ciudades.keys()

while len(ciudades)<5:
    nombre=input("Nombre ciudad: ")
    #si la ciudad no se ha repetido, se guarda
    if not ciudad_repetida(nombre):
        temp=float(input("Temperatura ciudad: "))
        ciudades[nombre]=temp
    else:
        print("No vale, ciudad repetida")
print(ciudades)  

print("Temperatura media: ",sum(ciudades.values())/len(ciudades))  

#temp_min=ciudades[nombre] #se inicializa con una de las temperaturas existentes
temp_min=list(ciudades.values())[0]
ciudad_fria=None
for k,v in ciudades.items():
    if v<=temp_min:
        ciudad_fria=k
        temp_min=v
print("La ciudad más fría es: ",ciudad_fria)

    