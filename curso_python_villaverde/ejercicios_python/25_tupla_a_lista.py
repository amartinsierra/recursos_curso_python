#dada la siguiente tupla:
valores=(4,11,2,4,7,2,10,7,1)
#crear una lista con los valores de esa tupla, sin números repetidos
lista_final=[]
def repetido(lista, numero):
    rep=False
    for n in lista:
        if numero==n:
            rep=True
    return rep

for n in valores:
    if repetido(lista_final,n)==False:
        lista_final.append(n)
print(lista_final)
