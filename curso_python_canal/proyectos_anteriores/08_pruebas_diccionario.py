alumno={"nombre":"alumno1","curso":"Python","nota":7.8}
alumno["email"]="al@gmail.com"
print(alumno)
for k in alumno.keys():
    print(k)
for v in alumno.values():
    print(v)
for k,v in alumno.items():
    print(k,"-",v)