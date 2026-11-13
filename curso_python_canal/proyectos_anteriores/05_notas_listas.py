#dada una lista de notas, indicar cuantos aprobados hay
notas=[7.2,6.4,2.7,9.0,3.4,1.5,6.7]
total_aprobados=0
for n in notas:
    if n>=5:
        total_aprobados+=1 #total_aprobados=total_aprobados+1
print("total de aprobados: ",total_aprobados)
print("nota más alta ",max(notas))
print("nota más baja ",min(notas))
print("nota media ",sum(notas)/len(notas))

