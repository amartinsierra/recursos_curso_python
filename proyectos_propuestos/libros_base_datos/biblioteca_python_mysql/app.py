import mysql.connector
from libros import insertar_libro, listar_libros, buscar_libros, eliminar_libro
from socios import insertar_socio, listar_socios
from prestamos import registrar_prestamo, listar_prestamos_activos, historial_socio, registrar_devolucion

def mostrar_libros():
    print("\n--- LIBROS ---")
    for libro in listar_libros():
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f'{libro["id"]}: {libro["titulo"]} | {libro["autor"]} | {libro["anyo"]} | {estado}')

def mostrar_socios():
    print("\n--- SOCIOS ---")
    for socio in listar_socios():
        print(f'{socio["id"]}: {socio["nombre"]} ({socio["email"]})')

def menu():
    while True:
        print("""
========= BIBLIOTECA =========
1. Añadir libro
2. Mostrar libros
3. Buscar libros
4. Eliminar libro
5. Registrar socio
6. Mostrar socios
7. Registrar préstamo
8. Mostrar préstamos activos
9. Historial de un socio
10. Registrar devolución
0. Salir
""")
        opcion = input("Opción: ").strip()
        try:
            if opcion == "1":
                titulo = input("Título: ").strip()
                autor = input("Autor: ").strip()
                texto_anyo = input("Año (opcional): ").strip()
                anyo = int(texto_anyo) if texto_anyo else None
                print("Libro creado con ID", insertar_libro(titulo, autor, anyo))
            elif opcion == "2":
                mostrar_libros()
            elif opcion == "3":
                for libro in buscar_libros(input("Texto a buscar: ").strip()):
                    print(f'{libro["id"]}: {libro["titulo"]} - {libro["autor"]}')
            elif opcion == "4":
                if eliminar_libro(int(input("ID del libro: "))):
                    print("Libro eliminado.")
                else:
                    print("No se ha eliminado: no existe o tiene préstamos asociados.")
            elif opcion == "5":
                nombre = input("Nombre: ").strip()
                email = input("Email: ").strip()
                print("Socio creado con ID", insertar_socio(nombre, email))
            elif opcion == "6":
                mostrar_socios()
            elif opcion == "7":
                mostrar_libros()
                mostrar_socios()
                libro_id = int(input("ID del libro: "))
                socio_id = int(input("ID del socio: "))
                print("Préstamo creado con ID", registrar_prestamo(libro_id, socio_id))
            elif opcion == "8":
                print("\n--- PRÉSTAMOS ACTIVOS ---")
                for p in listar_prestamos_activos():
                    print(f'{p["id"]}: {p["titulo"]} - {p["nombre"]} (desde {p["fecha_prestamo"]})')
            elif opcion == "9":
                socio_id = int(input("ID del socio: "))
                for p in historial_socio(socio_id):
                    print(f'{p["id"]}: {p["titulo"]} | préstamo: {p["fecha_prestamo"]} | devolución: {p["fecha_devolucion"]}')
            elif opcion == "10":
                registrar_devolucion(int(input("ID del préstamo: ")))
                print("Devolución registrada.")
            elif opcion == "0":
                print("Hasta pronto.")
                break
            else:
                print("Opción no válida.")
        except ValueError as error:
            print("Operación no realizada:", error)
        except mysql.connector.IntegrityError as error:
            print("Error de integridad:", error)
        except mysql.connector.Error as error:
            print("Error de MySQL:", error)
        except Exception as error:
            print("Error:", error)

if __name__ == "__main__":
    menu()
