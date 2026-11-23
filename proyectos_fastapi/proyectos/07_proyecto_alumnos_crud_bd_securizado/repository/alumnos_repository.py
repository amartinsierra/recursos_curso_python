from model.alumnos_model import AlumnoEntity
from config.db_config import connection_pool
class AlumnoRepository:
    def save(self,alumno:AlumnoEntity):
        sql="insert into alumnos (nombre,curso,nota,email) values(%s,%s,%s,%s)"
        con=connection_pool.get_connection()
        cursor=con.cursor()
        cursor.execute(sql,(alumno.nombre,
                            alumno.curso,
                            alumno.nota,
                            alumno.email))
        alumno.idAlumno=cursor.lastrowid
        con.commit()
        con.close()
        return alumno
    def findAll(self):
        sql="select * from alumnos"
        con=connection_pool.get_connection()
        cursor=con.cursor(dictionary=True)
        cursor.execute(sql)
        alumnos=cursor.fetchall()
        con.close()
        return alumnos
    def findByEmail(self,email:str):
        sql="select * from alumnos where email=%s"
        con=connection_pool.get_connection()
        cursor=con.cursor(dictionary=True)
        cursor.execute(sql,(email,))
        alumno=cursor.fetchone()
        con.close()
        return alumno
    def findByCurso(self,curso:str):
        sql="select * from alumnos where curso=%s"
        con=connection_pool.get_connection()
        cursor=con.cursor(dictionary=True)
        cursor.execute(sql,(curso,))
        alumnos=cursor.fetchall()
        con.close()
        return alumnos
    def deleteByEmail(self,email:str):
        sql="delete from alumnos where email=%s"
        con=connection_pool.get_connection()
        cursor=con.cursor()
        cursor.execute(sql,(email,))
        con.commit()
        con.close()