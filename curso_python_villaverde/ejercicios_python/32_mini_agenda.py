"""
 Programa agenda de nombres
 El programa muestra el siguiente menú:
 1.- Nuevo nombre
 2.- Mostrar todos
 3.- Comprobar contacto
 4.-Salir
 
 si se selecciona 1, se pide el nombre y se guarda en el fichero
 si se selecciona 2, se muestran todos los nombres
 se se selecciona 3, se pide el nombre de un contacto y el programa nos dirá si existe
 o no en el fichero
    
"""
ruta_fichero="nombres.txt"
def opcion1():
    f=open(ruta_fichero,"a")
    nombre=input("Escribe el nombre del contacto:")
    f.write(nombre)
    f.write("\n")
    f.close()
def opcion2():    
    try:
        f=open(ruta_fichero,"r")
        nombre=f.readline()
        while nombre!="":
            print("Contacto: ",nombre)
            nombre=f.readline()
        f.close()
    except FileNotFoundError:
        print("El fichero aún no existe, debe añadir al menos un contacto")
def opcion3():
    nombre_buscar=input("Dime el nombre que buscas ")
    encontrado=False #en esta variable guardo el resultado de la búsqueda
    try:
        f=open(ruta_fichero,"r")
        nombre=f.readline().rstrip("\n")
        while nombre!="":
            if nombre==nombre_buscar: #lo hemos encontrado
                encontrado=True
            nombre=f.readline().rstrip("\n")
        if encontrado==True:
            print("El contacto está en la agenda")
        else:
            print("El contacto no está en la agenda")
        f.close()
    except FileNotFoundError:
        print("El fichero aún no existe, debe añadir al menos un contacto")
    except FileExistsError:
        print()
def mostrar_menu():
    print("1.- Nuevo nombre ")
    print("2.- Mostrar todos ")
    print("3.- Comprobar contacto")
    print("4.- Salir ")
    return input()
while True:
    opcion=mostrar_menu()
    if opcion=="1":
        opcion1()
    elif opcion=="2":
        opcion2()
    elif opcion=="3":
        opcion3()
    elif opcion=="4":
        break #salida forzada de la instrucción while
