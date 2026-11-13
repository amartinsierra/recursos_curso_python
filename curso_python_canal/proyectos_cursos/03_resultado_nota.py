#lee la nota de un alumno y dice si está aprobado o suspenso
nota=input("Introduce nota del alumno ")
#convertir número a texto
nota=int(nota)
if nota>=5:
    print("aprobado")
else:
    print("Suspenso")