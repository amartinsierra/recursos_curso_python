#realizar un programa que realice la funcionalidad de un cajero
#Menu:
#1. Ingresar
#2. Extraer
#3. Ver saldo
#4. Salir

class Cuenta_Bancaria:
    saldo=0
    def __init__(self,s):
        self.saldo=s
    def ingresar(self,cantidad):
        self.saldo=self.saldo+cantidad
    def extraer(self,cantidad):
        self.saldo=self.saldo-cantidad


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1 - Ingresar")
    print("2 - Extraer")
    print("3 - Ver saldo")
    print("4 - Salir")
    return input("Elige una opción: ")

#creamos objeto Cuenta_Bancaria
saldo_inicial=float(input("Introduce saldo inicial"))
cuenta=Cuenta_Bancaria(saldo_inicial)
while True:
    opcion = mostrar_menu()   
    if opcion == "1":
        cantidad=float(input("Introduce cantidad: "))
        cuenta.ingresar(cantidad)
    elif opcion == "2":
        cantidad=float(input("Introduce cantidad: "))
        cuenta.extraer(cantidad)
    elif opcion == "3":
        print("El saldo es: ",cuenta.saldo)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")