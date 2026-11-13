import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="TU_PASSWORD",  # Sustituir por la contraseña de MySQL
        database="biblioteca"
    )
