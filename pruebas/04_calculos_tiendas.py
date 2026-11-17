
import pandas as pd

df = pd.read_csv("ventas_tiendas.csv")


# 1. Facturación total de una tienda
def facturacion_tienda(nombre):
    datos = df.query("`nombre tienda` == @nombre")

    if datos.empty:
        print("No existe esa tienda")
        return

    print(f"Facturación total: {datos['facturacion'].sum()} €")


# 2. Tienda con mayor gasto de personal
def mayor_gasto_personal():
    gastos = df.groupby("nombre tienda")["gastos personal"].sum()

    gastos = gastos.sort_values(ascending=False)

    resultados = gastos.to_dict()
    tienda = list(resultados.keys())[0]

    print(f"Tienda: {tienda}")
    print(f"Gasto total: {resultados[tienda]} €")


# 3. Facturación total por meses
def facturacion_meses():
    resultado = df.groupby("mes")["facturacion"].sum()

    print(resultado.to_dict())


# 4. Mes con mayor facturación de una tienda
def mejor_mes(nombre):
    datos = df.query("`nombre tienda` == @nombre")

    if datos.empty:
        print("No existe esa tienda")
        return

    datos = datos.sort_values("facturacion", ascending=False)

    resultado = datos.to_dict(orient="records")[0]

    print(f"Mes: {resultado['mes']}")
    print(f"Facturación: {resultado['facturacion']} €")


# Menú principal
while True:
    print("\n1. Facturación de una tienda")
    print("2. Tienda con mayor gasto de personal")
    print("3. Facturación total por meses")
    print("4. Mejor mes de una tienda")
    print("0. Salir")

    opcion = input("\nOpción: ")

    if opcion == "1":
        facturacion_tienda(input("Nombre de tienda: "))

    elif opcion == "2":
        mayor_gasto_personal()

    elif opcion == "3":
        facturacion_meses()

    elif opcion == "4":
        mejor_mes(input("Nombre de tienda: "))

    elif opcion == "0":
        break

    else:
        print("Opción incorrecta")
