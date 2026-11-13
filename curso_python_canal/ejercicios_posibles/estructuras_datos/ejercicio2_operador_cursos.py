import datetime
cursos=[]
op=0
def menu():
    print("1.- Nuevo curso")
    print("2.- Eliminar curso")
    print("3.- Cursos por fecha")
    print("4.- Salir")
def nuevocurso():
    curso={}
    curso["Nombre"]=input("Nombre del curso: ")
    curso["Duracion"]=input("Duración del curso: ")
    curso["Fecha"]=input("Fecha del curso(año-mes-dia): ")
    return curso
def eliminarcurso():
    nombre=input("Introduce el nombre del curso a eliminar: ")
    for c in cursos:
        if c["Nombre"]==nombre:
            cursos.remove(c)
def filtrarfecha():
    fecha=input("Introduce fecha límite(año-mes-dia): ")
    fecha=datetime.datetime.strptime(fecha,"%Y-%m-%d")
    for c in cursos:
        if fecha>datetime.datetime.strptime(c["Fecha"],"%Y-%m-%d"):
            print(c["Nombre"],"-",c["Duracion"],"-",c["Fecha1"])
while op!="4":
    menu()
    op=input(" ")
    if op=="1":
        cursos.append(nuevocurso())
    elif op=="2":
        eliminarcurso()
    elif op=="3":
        filtrarfecha()
    
    
    
