import mysql.connector as con
db=con.connect(host="localhost",
               port="3307",
               user="root",
               password="root",
               database="academia")
cursor=db.cursor();
cursor.execute("select * from alumnos")
for c in cursor:
    print(c)
cursor.execute("select avg(nota) from alumnos")
for c in cursor:
    print("Nota media: ",c[0])
db.close()
