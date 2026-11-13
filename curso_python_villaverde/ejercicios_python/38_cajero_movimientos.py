#Crear una nueva versión del cajero, que incluya una nueva opción de menú:
"""
    1 - Ingresar
    2 - Extraer
    3 - Ver datos cuenta
    4.- Mostrar movimientos
    5 - Salir

Mostrar movimientos nos muestra los movimientos realizados en la cuenta:
operacion-cantidad


para ello, se creará una nueva clase, llamada Cuenta_Movimientos
que herede Cuenta_Mejorada y que incluya una atributo para guardar los movimientos
y algún que otro ajuste necesario...
"""

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

#programa principal      
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1 - Ingresar")
    print("2 - Extraer")
    print("3 - Ver datos cuenta")
    print("4 - Mostrar movimientos")
    print("5 - Salir")
    return input("Elige una opción: ")

#creamos objeto Cuenta_Bancaria
saldo_inicial=float(input("Introduce saldo inicial: "))
numero_cuenta=int(input("Introduce número cuenta: "))
cuenta=Cuenta_Movimientos(saldo_inicial,numero_cuenta)
while True:
    opcion = mostrar_menu()   
    if opcion == "1":
        cantidad=float(input("Introduce cantidad: "))
        cuenta.ingresar(cantidad)
    elif opcion == "2":
        cantidad=float(input("Introduce cantidad: "))
        cuenta.extraer(cantidad)
    elif opcion == "3":
        res=cuenta.generar()
        print("Datos de la cuenta: ",res["saldo"])
    elif opcion == "4":
        #print(cuenta.movimientos)  
        for m in cuenta.movimientos:
            print(m["tipo"],"-",m["cantidad"])
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")