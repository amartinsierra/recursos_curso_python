from conexion import obtener_conexion

def insertar_libro(titulo, autor, anyo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO libros (titulo, autor, anyo) VALUES (%s, %s, %s)",
            (titulo, autor, anyo)
        )
        conexion.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conexion.close()

def listar_libros():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM libros ORDER BY titulo")
        return cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()

def buscar_libros(texto):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    try:
        parametro = f"%{texto}%"
        cursor.execute(
            "SELECT * FROM libros WHERE titulo LIKE %s OR autor LIKE %s ORDER BY titulo",
            (parametro, parametro)
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()

def eliminar_libro(libro_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM prestamos WHERE libro_id = %s", (libro_id,))
        if cursor.fetchone()[0] > 0:
            return False
        cursor.execute("DELETE FROM libros WHERE id = %s", (libro_id,))
        conexion.commit()
        return cursor.rowcount == 1
    finally:
        cursor.close()
        conexion.close()
