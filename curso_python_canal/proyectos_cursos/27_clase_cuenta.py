class cuenta_bancaria:
    saldo=0
    codigo=111
    #constructor
    def __init__(self,s,c):
        self.saldo=s
        self.codigo=c
    def ingresar(self,cantidad):
        self.saldo=self.saldo+cantidad
    def extraer(self,cantidad):
        self.saldo=self.saldo-cantidad
    def leer_saldo(self):
        return self.saldo
    
#creamos objeto cuenta bancaria
cuenta=cuenta_bancaria(200,99999)
cuenta.ingresar(10)
cuenta.ingresar(20)
cuenta.extraer(40)
print(cuenta.leer_saldo())

#HERENCIA

class cuenta_movimientos(cuenta_bancaria):
    movimientos=[]
    def recupera_movimientos(self):
        return self.movimientos
    
    #SOBRESCRITURA DE METODOS
    def ingresar(self,cantidad):
        self.movimientos.append({"tipo":"ingreso","cantidad":cantidad})
        super().ingresar(cantidad)
    def extraer(self,cantidad):
        self.movimientos.append({"tipo":"extracción","cantidad":cantidad})
        super().extraer(cantidad)