empleados=[
    {"nombre":"emp1","departamento":"informática","salario":2300,"edad":31},
    {"nombre":"emp2","departamento":"RRHH","salario":1900,"edad":24},
    {"nombre":"emp3","departamento":"informática","salario":1840,"edad":54},
    {"nombre":"emp4","departamento":"ventas","salario":2450,"edad":46},
    {"nombre":"emp5","departamento":"ventas","salario":1930,"edad":32},
    {"nombre":"emp6","departamento":"informática","salario":2200,"edad":45},
    {"nombre":"emp7","departamento":"RRHH","salario":1980,"edad":61},
    {"nombre":"emp8","departamento":"informática","salario":1700,"edad":29}
]
#indica si existe un empleado a partir del nombre recibido
def existeEmpleado(nombre):
    return nombre in list(map(lambda e:e["nombre"],empleados))

#devuelve una lista con los empleados del departamento recibido
def empleadosPorDepartamento(dep):
    return list(filter(lambda e:e["departamento"]==dep,empleados)),
#devuelve una lista con los nombres de los departamentos
def departamentos():
    return set(map(lambda e:e["departamento"],empleados))
#devuelve la media de salarios
def salarioMedio():
    salarios=list(map(lambda e:e["salario"],empleados))
    return sum(salarios)/len(salarios)
#devuelve la media de edad del departamento recibido
def mediaEdadDepartamento(departamento):
    edades=list(map(lambda e:e["edad"],list(filter(lambda e:e["departamento"]==departamento,empleados))))
    return sum(edades)/len(edades)
#devuelve la lista de empleados, ordenados por salario
def ordenarPorSalario():
   return list(map(lambda e:(e["nombre"],e["salario"]),sorted(empleados,key=lambda e:e["salario"])))
    
print(ordenarPorSalario())   