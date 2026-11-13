import pymongo
uri="mongodb://localhost:27017"
def menu():
    print("1. Alta de libro")
    print("2. Buscar libro")
    print("3. Libros por precio máximo")
    print("4. Salir")
def consultarporisbn(isbn):
    serv=pymongo.MongoClient(uri)
    db=serv.libreria
    lib=db.libros.find_one({"isbn":isbn})
    serv.close()
    if lib!=None:
        return True
    return False
def altalibro(isbn,titulo,tematica,precio):
    serv=pymongo.MongoClient(uri)
    db=serv.libreria
    db.libros.insert_one({"isbn":isbn,"titulo":titulo,"tematica":tematica,"precio":precio})
    serv.close()
def buscarlibro(isbn):
    serv=pymongo.MongoClient(uri)
    db=serv.libreria
    libro=db.libros.find_one({"isbn":isbn})  
    serv.close() 
    return libro
    
    
def librospreciomaximo(precio):
    serv=pymongo.MongoClient(uri)
    db=serv.libreria
    libros=db.libros.find({"precio":{"$lte":precio}})
    libros=list(libros)
    # for l in libros:
    #     libros.append(l)  
    serv.close()
    return libros

opcion=0
while opcion!=4:
    menu()
    opcion=int(input("Introduce opción: "))
    if opcion==1:
        isbn=int(input("Introduce Isbn del libro: "))
        while consultarporisbn(isbn):
            print("Isbn ya existente, introduce un nuevo")
            isbn=int(input("Introduce otro Isbn del libro: "))
        titulo=input("Introduce título de libro: ")
        tematica=input("Introduce la temática del libro: ")
        precio=float(input("Introduce precio del libro: "))
        
        altalibro(isbn,titulo,tematica,precio)
    elif opcion==2:
        isbn=int(input("Introduce isbn: "))
        libro=buscarlibro(isbn)
        if libro!=None:        
            print("Titulo: ",libro["titulo"],"Isbn: ",libro["isbn"],"Temática: ",libro["tematica"],"Precio: ",libro["precio"])
        else:
            print("No existe ese libro!")
    elif opcion==3:
        precio=float(input("Introduce precio máximo: "))
        libros=librospreciomaximo(precio)
        for l in libros:
            print("Titulo: ",l["titulo"],"Isbn: ",l["isbn"],"Temática: ",l["tematica"],"Precio: ",l["precio"])
    
    