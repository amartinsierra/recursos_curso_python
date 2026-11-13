op=""
num=int(input("Introduce un número: "))
def primo(dato):
    res=True
    for n in range(2,dato):
        if(dato%n==0):
            res=False
    return res
def factorial(dato):
    res=1
    for n in range(2,dato+1):
        res*=n
    return res
def menu():
    print("1. Calcular si primo")
    print("2. Calcular factorial")
    print("3. Nuevo número")
    print("4. Salir")
    
while op!="4":
    menu()
    op=input("")
    if op=="1":
        if primo(num):
            print("El número ",num," es primo")
        else:
            print("El número ",num," no es primo")
    elif op=="2":
        print("El factorual de ",num, "es ",factorial(num))
    elif op=="3":
        num=int(input("Introduce un nuevo número"))
    