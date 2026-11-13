#import clases as c
from clases import Cuenta_Movimientos


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