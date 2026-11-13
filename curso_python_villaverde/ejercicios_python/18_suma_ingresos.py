import numpy as np

ingresos=[100,65,30,86]
ingresos[3:4]=[123,45]
print(ingresos)
#calcular el total de ingresos obtenidos
"""
suma=0
for n in ingresos:
    suma=suma+n  #suma+=n
print("El total de ingresos ha sido: ",suma)
"""

print([n+1 for n in range(1,8) if n%2==0])
cad="5,2,7,4"
print(max(map(lambda n:int(n),cad.split(","))))
a1=np.array([3,5,7,10,1])
a2=np.array([1,0,4,8,2])
print(np.add(a1,a2)) #[4,511,18,3]
