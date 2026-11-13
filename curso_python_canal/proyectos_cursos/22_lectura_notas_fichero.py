dir="c:\\tmp\\notas.txt"
try:
    f=open(dir,"r")
    #print(f.readlines())
    notas=list(map(lambda n:float(n.strip()) ,f.readlines()))
    print("Nota media: ",sum(notas)/len(notas))
    f.close()
except FileNotFoundError:
    print("el fichero ya no existe!")
