import mysql.connector
host="localhost"
user="root"
password="root"
port="3307"
database="productos"
def menu():
    print("1. Nuevo producto")
    print("2. Buscar por categoría")
    print("3. Eliminar producto")
    print("4. Modificar precio")
    print("5.- Salir")
def consultarproducto(codigo):
    db=mysql.connector.connect(host=host,
                               user=user,
                               password=password,
                               port=port,
                               database=database)
    cursordb=db.cursor()
    sql="select * from productos where codProducto=%s"
    cursordb.execute(sql,(codigo,))
    for p in cursordb:
        db.close()
        return True
    db.close()
    return False

def nuevoproducto(codigo,nombre,categoria,preciounitario,stock):
    db=mysql.connector.connect(host=host,
                               user=user,
                               password=password,
                               port=port,
                               database=database)
    cursordb=db.cursor()
    sql="insert into productos values(%s,%s,%s,%s,%s)"
    cursordb.execute(sql,(codigo,nombre,categoria,preciounitario,stock))
    db.commit()
    db.close()
def buscarporcategoria(categoria):
    db=mysql.connector.connect(host=host,
                               user=user,
                               password=password,
                               port=port,
                               database=database)
    cursordb=db.cursor()
    sql="select * from productos where categoria=%s"
    cursordb.execute(sql,(categoria,))
    for p in cursordb:
        print(p)

def eliminar(codigo):
    db=mysql.connector.connect(host=host,
                               user=user,
                               password=password,
                               port=port,
                               database=database)
    cursordb=db.cursor()
    sql="delete from productos where codProducto=%s"
    cursordb.execute(sql,(codigo,))
    db.commit()
    db.close()

def modificarprecio(codigo,nuevoprecio):
    db=mysql.connector.connect(host=host,
                               user=user,
                               password=password,
                               port=port,
                               database=database)
    cursordb=db.cursor()
    sql="update productos set precioUnitario=%s where codProducto=%s"
    cursordb.execute(sql,(nuevoprecio,codigo))
    db.commit()
    db.close()
opcion=0
while opcion!=5:
    menu()
    opcion=int(input("Introduce opción: "))
    if opcion==1:
        codigo=input("Introduce código de producto: ")
        while consultarproducto(codigo):
            print("Código ya existente, introduce un nuevo")
            codigo=input("Introduce otro código de producto: ")
        nombre=input("Introduce nombre de producto: ")
        categoria=input("Introduce la categoría del producto: ")
        precio=input("Introduce precio unitario del producto: ")
        stock=input("Introduce stock producto: ")
        nuevoproducto(codigo,nombre,categoria,precio,stock)
    elif opcion==2:
        categoria=input("Introduce categoria: ")
        buscarporcategoria(categoria)
    elif opcion==3:
        codigo=input("Introduce código del producto a eliminar: ")
        eliminar(codigo)
    elif opcion==4:
        codigo=input("Introduce código de producto: ")
        while not consultarproducto(codigo):
            print("El código no existe, introduce un nuevo")
            codigo=input("Introduce otro código de producto: ")
        precio=input("Introduce nuevo precio de producto: ")
        modificarprecio(codigo,precio)
    