f=open("nombres.txt","w") #para resetear el fichero cada vez que se inicia el programa
def existeNombre(nombre):
    f=open("nombres.txt","r")
    l=f.readline()
    while l!="":
        l=l.replace("\n","")
        if l==nombre:
            return True
        l=f.readline()
    return False

def grabaNombre(nombre):
    f=open("nombres.txt","a")
    f.write(nombre+"\n") #cada nombre en una línea
        
total=0
while total<10:
    nombre=input("Introduce un nombre:")
    if not existeNombre(nombre):
        grabaNombre(nombre)
        total+=1
    else:
        print("Ese nombre ya existe")

