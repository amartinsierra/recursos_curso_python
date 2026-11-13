from conexion import obtener_conexion

def insertar_socio(nombre, email):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO socios (nombre, email) VALUES (%s, %s)",
            (nombre, email)
        )
        conexion.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conexion.close()

def listar_socios():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM socios ORDER BY nombre")
        return cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()
