"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo presio sea igual o inferior a ese precio
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
"""
#crea funciones para cada tarea.
libros=[]
def nuevo_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    try:
        precio = float(input("Precio: "))
    except ValueError:
        print("Precio no válido. No se agregó el libro.")
        return
    libros.append({"titulo": titulo, "autor": autor, "precio": precio})
    print("Libro agregado.")

def titulos():
    if not libros:
        print("No hay libros en la librería.")
    else:
        print("Títulos de los libros:")
        for i in libros:
            print(i["titulo"])
                    
def buscar_titulo():
    buscar=input("Introduce el titulo del libro que quieres buscar: ")
    encontrado=False
    
    for i in libros:
        if buscar.lower() == i["titulo"].lower():
            print("Se ha encontrado tu libro")
            print("Título: ",i["titulo"],"Autor: ",i["autor"],"Precio: ",i["precio"])
            encontrado= True
    if not encontrado:
        print("Libro no encontrado")
        
def libros_por_precio_maximo():
    try:
        max_precio = float(input("Precio máximo: "))
    except ValueError:
        print("Precio no válido.")
        return
    titulos = []
    for n in libros:
        if n["precio"] <= max_precio:
            titulos.append(n["titulo"])
    if titulos:
        print(f"Libros con precio <= {max_precio}:")
        for j in titulos:
            print(j)  
    else:
        print("No hay libros con ese precio o inferior.")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1 - Nuevo libro")
    print("2 - Mostrar todos")
    print("3 - Buscar por título")
    print("4 - Libros por precio máximo")
    print("5 - Salir")
    return input("Elige una opción: ")

while True:
    opcion = mostrar_menu()
    
    if opcion == "1":
        nuevo_libro()
    elif opcion == "2":
        titulos()
    elif opcion == "3":
        buscar_titulo()
    elif opcion == "4":
        libros_por_precio_maximo()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")