import csv
f=open("coordenadas.csv","r")
next(f)
for n in csv.reader(f):  
    print(n)