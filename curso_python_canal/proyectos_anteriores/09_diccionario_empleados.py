def menu():
    print("1.-Nuevo empleado")
    print("2.-Buscar empleado")
    print("3.-Salir")
def buscar_empleado(lista,dni):
    empleado=None
    for e in lista:
        if e["dni"]==dni:
            empleado=e
    return empleado
empleados=[]
opcion=0
while opcion!="3":
    menu()
    opcion=input("")
    if(opcion=="1"):
        #pedir datos del empleado y guardarlo como un diccionario dentro de la lista
        emp={}
        emp["nombre"]=input("Introduce nombre: ")
        emp["dni"]=input("Introduce dni: ")
        emp["salario"]=input("Introduce salario: ")
        empleados.append(emp)
    elif(opcion=="2"):
        #pedir el dni y buscar si algun empleado de la lista tiene ese dni y y mostrar sus datos
        dni=input("Introduce el DNI")
        empl=buscar_empleado(empleados,dni)
        #si encontró el empleado, muestra sus datos
        if empl:
            print(empl)
        else:
            print("No encontrado")