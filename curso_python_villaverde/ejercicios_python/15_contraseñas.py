#solicita la introducción de una contraseña, si es correcta
#le dice que es un usuario válido. Si no es correcta, se le vuelve a pedir.
#Así, hasta tres intentos. Si después del tercer intento la contraseña es incorrecta
#le dice que no es un usuario válido

password="admin"
intentos=3
acertado=False
while intentos>0 and acertado==False:
    contra=input("Introduce contraseña ")
    if contra==password:
        acertado=True
    else:
        print("Vuelve a intentar!")
        intentos=intentos-1
if acertado==True:
    print("Usuario válido!")
else:
    print("Usuario no válido!")