from conexion import obtener_conexion


def obtener_notas():
    """Devuelve todas las calificaciones como una lista de diccionarios."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, alumno, asignatura, nota, fecha
            FROM notas
            ORDER BY alumno, asignatura, fecha
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()
