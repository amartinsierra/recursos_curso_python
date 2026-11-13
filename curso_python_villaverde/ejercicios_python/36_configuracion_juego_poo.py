#Configuración de un juego
#Realizar un programa que se encargue de configurar un juego 
#La configuración consisitirá en:
#Crear dos personajes. Cada personaje tiene un nombre y un rol
#Crear tres armas. Cada arma, tiene un nombre un poder y una función
#que es atacar
#Los nombre de personajes y armas, así como los roles y poderes, se le piden
#al usuario por teclado
class Personaje:
    nombre=""
    rol=""
    def __init__(self,n,r):
        self.nombre=n
        self.rol=r
class Arma:
    nombre=""
    poder=0
    def __init__(self,n,p):
        self.nombre=n
        self.poder=p
    def atacar(self):
        print("Atacando con el arma",self.nombre)

p1=Personaje("personaje 1","enemigo")
p2=Personaje("personaje 2","brujo")

a1=Arma("espada",4)
a2=Arma("lanza",3)
a3=Arma("cañón",7)