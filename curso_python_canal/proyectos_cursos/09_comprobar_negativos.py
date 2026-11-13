lista=[9,21,11,3,-4,8,34]
#¿Hay algún número negativo?
indicador=False
for n in lista:
    if n<0:
        indicador=True
        break
print("¿Hay negativos? ",indicador)