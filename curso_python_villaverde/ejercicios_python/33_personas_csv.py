#programa que muestre los nombres de todos los empleados que hay en el archivo empresa.csv
import csv
f=open("empresa.csv","r",encoding="UTF-8")
reader=csv.reader(f) #un iterador
next(reader)
for p in reader:
    print(p[0])
print("-------------------")
f.close()
f=open("empresa.csv","r",encoding="UTF-8")
dictReader=csv.DictReader(f)
for p in dictReader:
    print(p["empleado"])
f.close()
