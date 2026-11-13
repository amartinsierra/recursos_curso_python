emails=["mycar@gmail.com","iss@printer.es","cabi@gmail.com","beer@scape.es"]
#mostrar las direcciones de email que sean de España

print(list(filter(lambda e:e.endswith(".es"),emails)))


palabras="casa,bolígrafo,escaparate,prensa,vino,boca,amarillo";
#mostrar las palabras que tienen más de 6 caracteres
print(list(filter(lambda p:len(p)>6,palabras.split(","))))