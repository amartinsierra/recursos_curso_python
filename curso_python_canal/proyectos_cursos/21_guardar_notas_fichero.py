dir="c:\\tmp\\notas.txt"
notas=[4.5,2.7,8.9,5.6,3.3]
#guardamos las notas en un fichero. Cada una en una línea
f=open(dir,"w")
for n in notas:
    f.write(str(n)+"\n")
f.close() #cerramos fichero al terminar