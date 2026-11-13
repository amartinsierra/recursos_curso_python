#mejora del cajero, donde haya una nueva clase que herede Cuenta_bancaria
#que incluya el número de cuenta
#y un método generar que devuelva un JSON con los datos de la cuenta


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
    
    
#programa principal      
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1 - Ingresar")
    print("2 - Extraer")
    print("3 - Ver datos cuenta")
    print("4 - Salir")
    return input("Elige una opción: ")

#creamos objeto Cuenta_Bancaria
saldo_inicial=float(input("Introduce saldo inicial"))
numero_cuenta=int(input("Introduce número cuenta"))
cuenta=Cuenta_Mejorada(saldo_inicial,numero_cuenta)
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
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")