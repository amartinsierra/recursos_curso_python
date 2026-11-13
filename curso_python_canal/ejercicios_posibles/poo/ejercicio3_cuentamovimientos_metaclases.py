import datetime
class Cuenta:
    saldo=0
    def __init__(self,saldo=100):
        self.saldo=saldo
    def ingresar(self,cantidad):
        self.saldo+=cantidad
    def extraer(self,cantidad):
        self.saldo-=cantidad
class Movimiento:
    cantidad=0
    tipo=""
    fecha=""
    def __init__(self,cantidad,tipo,fecha):
        self.cantidad=cantidad
        self.tipo=tipo
        self.fecha=fecha

def ingresar(self,cantidad):
    self.movimientos.append(Movimiento(cantidad,"ingreso",datetime.datetime.today()))
    super(CuentaMovimientos,self).ingresar(cantidad)
def extraer(self,cantidad):
    self.movimientos.append(Movimiento(cantidad,"extracción",datetime.datetime.today()))
    super(CuentaMovimientos,self).extraer(cantidad)

CuentaMovimientos=type("CuentaMovimientos",(Cuenta,),{"movimientos":[],"ingresar":ingresar,"extraer":extraer})       
ct=CuentaMovimientos(500)
ct.ingresar(200)
ct.extraer(150)
ct.extraer(100)
movs=ct.movimientos
for m in movs:
    print(m.cantidad,m.tipo,m.fecha)

print("El saldo final es: ", ct.saldo)