import polars as pl

df = pl.read_csv("ventas_tiendas.csv")


# 1. Facturación total de una tienda
def facturacion_tienda(nombre):
    datos = df.filter(pl.col("nombre tienda") == nombre)

    if datos.is_empty():
        print("No existe esa tienda")
        return

    total = datos["facturacion"].sum()

    print(f"Facturación total: {total} €")


# 2. Tienda con mayor gasto de personal
def mayor_gasto_personal():
    gastos = (
        df.group_by("nombre tienda")
          .agg(pl.col("gastos personal").sum().alias("total"))
          .sort("total", descending=True)
    )

    resultado = gastos.row(0, named=True)

    print(f"Tienda: {resultado['nombre tienda']}")
    print(f"Gasto total: {resultado['total']} €")


# 3. Facturación total por meses
def facturacion_meses():
    resultado = (
        df.group_by("mes")
          .agg(pl.col("facturacion").sum().alias("total"))
          .sort("mes")
    )

    print(resultado.to_dicts())


# 4. Mes con mayor facturación de una tienda
def mejor_mes(nombre):
    datos = df.filter(pl.col("nombre tienda") == nombre)

    if datos.is_empty():
        print("No existe esa tienda")
        return

    resultado = (
        datos.sort("facturacion", descending=True)
             .row(0, named=True)
    )

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
