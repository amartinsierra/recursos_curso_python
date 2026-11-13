from datetime import date
from conexion import obtener_conexion

def registrar_prestamo(libro_id, socio_id):
    """Inserta el préstamo y actualiza disponibilidad en una transacción."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        conexion.start_transaction()
        # FOR UPDATE bloquea el registro del libro mientras se valida y presta.
        cursor.execute("SELECT disponible FROM libros WHERE id = %s FOR UPDATE", (libro_id,))
        libro = cursor.fetchone()
        if libro is None:
            raise ValueError("No existe ese libro.")
        if not libro[0]:
            raise ValueError("El libro no está disponible.")

        cursor.execute("SELECT id FROM socios WHERE id = %s", (socio_id,))
        if cursor.fetchone() is None:
            raise ValueError("No existe ese socio.")

        cursor.execute(
            "INSERT INTO prestamos (libro_id, socio_id, fecha_prestamo) VALUES (%s, %s, %s)",
            (libro_id, socio_id, date.today())
        )
        cursor.execute("UPDATE libros SET disponible = FALSE WHERE id = %s", (libro_id,))
        conexion.commit()
        return cursor.lastrowid
    except Exception:
        conexion.rollback()
        raise
    finally:
        cursor.close()
        conexion.close()

def listar_prestamos_activos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT p.id, l.titulo, s.nombre, p.fecha_prestamo
            FROM prestamos p
            JOIN libros l ON p.libro_id = l.id
            JOIN socios s ON p.socio_id = s.id
            WHERE p.fecha_devolucion IS NULL
            ORDER BY p.fecha_prestamo
        """)
        return cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()

def historial_socio(socio_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT p.id, l.titulo, p.fecha_prestamo, p.fecha_devolucion
            FROM prestamos p
            JOIN libros l ON p.libro_id = l.id
            WHERE p.socio_id = %s
            ORDER BY p.fecha_prestamo DESC
        """, (socio_id,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conexion.close()

def registrar_devolucion(prestamo_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        conexion.start_transaction()
        cursor.execute("""
            SELECT libro_id FROM prestamos
            WHERE id = %s AND fecha_devolucion IS NULL
            FOR UPDATE
        """, (prestamo_id,))
        prestamo = cursor.fetchone()
        if prestamo is None:
            raise ValueError("No existe un préstamo activo con ese identificador.")

        libro_id = prestamo[0]
        cursor.execute("UPDATE prestamos SET fecha_devolucion = %s WHERE id = %s",
                       (date.today(), prestamo_id))
        cursor.execute("UPDATE libros SET disponible = TRUE WHERE id = %s", (libro_id,))
        conexion.commit()
    except Exception:
        conexion.rollback()
        raise
    finally:
        cursor.close()
        conexion.close()
