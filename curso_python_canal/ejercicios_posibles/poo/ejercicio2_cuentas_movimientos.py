import datetime
class Cuenta:
    saldo=0
    def __init__(self,saldo=0):
        self.saldo=saldo
    def ingresar(self,cantidad):
        self.saldo+=cantidad
    def extraer(self, cantidad):
        self.saldo-=cantidad
class Movimiento:
    cantidad=0
    tipo=""
    fecha=""
    def __init__(self,cantidad,tipo,fecha):
        self.cantidad=cantidad
        self.tipo=tipo
        self.fecha=fecha

class CuentaMovimiento(Cuenta):
    movimientos=[]
    def ingresar(self,cantidad):
        self.movimientos.append(Movimiento(cantidad,"ingreso",datetime.datetime.today()))
        super().ingresar(cantidad)
    def extraer(self,cantidad):
        self.movimientos.append(Movimiento(cantidad,"extracción",datetime.datetime.today()))
        super().extraer(cantidad)
        
cm=CuentaMovimiento(300)
cm.ingresar(50)
cm.extraer(10)
movs=cm.movimientos
for m in movs:
    print(m.tipo,m.cantidad)