class Cuenta_Bancaria:
    saldo=0
    def __init__(self,s):
        self.saldo=s
    def ingresar(self,cantidad):
        self.saldo=self.saldo+cantidad
    def extraer(self,cantidad):
        self.saldo=self.saldo-cantidad

class Cuenta_Mejorada(Cuenta_Bancaria):
    numero_cuenta=0
    def __init__(self,s,n):
        #self.saldo=s
        super().__init__(s) #llama a constructor de la clase base
        self.numero_cuenta=n
    def generar(self):
        return {"numero":self.numero_cuenta,"saldo":self.saldo}


class Cuenta_Movimientos(Cuenta_Mejorada):
    movimientos=[]
    def __init__(self, s, n):
        super().__init__(s, n)
    #sobrescribir ingresar y extraer para que además, graben 
    #el movimiento en la lista
    
    def ingresar(self, cantidad):
       super().ingresar(cantidad)
       self.movimientos.append({"tipo":"ingreso","cantidad":cantidad})
    def extraer(self,cantidad):
       super().extraer(cantidad)
       self.movimientos.append({"tipo":"extracción","cantidad":cantidad})