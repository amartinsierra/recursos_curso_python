class Cuenta:
    saldo=0
    def __init__(self,saldo=0):
        self.saldo=saldo
    def ingresar(self,cantidad):
        self.saldo+=cantidad
    def extraer(self, cantidad):
        self.saldo-=cantidad
        
c=Cuenta(100)
c.ingresar(30)
c.extraer(50)
print("El saldo de la cuenta es: ",c.saldo)