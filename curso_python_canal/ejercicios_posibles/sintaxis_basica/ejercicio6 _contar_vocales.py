frase=input("Introduce una frase: ")
vocales=0
minus=frase.lower()
for l in minus:
    #if l=="a" or l=="e" or l=="i" or l=="o" or l=="u":
    if l in ("a","e","i","o","u"):
        vocales+=1
print("La frase: ",frase, " tiene ",vocales," vocales")