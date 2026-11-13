import json
f=open("alumnos.json","r")
alumnos=json.load(f)
print(alumnos)