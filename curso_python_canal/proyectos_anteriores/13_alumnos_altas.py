import mysql.connector as con
db=con.connect(host="localhost",
               port="3307",
               user="root",
               password="root",
               database="academia")
cursor=db.cursor()
sql="insert into alumnos(nombre,curso,nota, email) values(%s,%s,%s,%s)"
valores=("profe python","bases de datos",5,"profe@gmail.com")
cursor.execute(sql,valores)
db.commit()
db.close()
print("Alumno guardado!")