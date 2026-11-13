nombres="Alicia,María,Alex,Marcos,Raúl,Gema,Rosa,Martín"
valores=nombres.split(",")
inicial=input("Introduce la inicial: ")
for c in valores:
    if c.startswith(inicial):
        print(c)