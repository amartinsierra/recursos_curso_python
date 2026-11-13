# Ejercicio: Aplicación de gestión de una biblioteca

## Contexto
Una pequeña biblioteca necesita una aplicación de consola en Python para gestionar libros, socios y préstamos. La información se almacenará en MySQL.

## Base de datos
La base de datos `biblioteca` tendrá tres tablas:

**LIBROS**: `id` (clave primaria), `titulo`, `autor`, `anyo`, `disponible` (1 disponible, 0 prestado).

**SOCIOS**: `id` (clave primaria), `nombre`, `email` (único).

**PRESTAMOS**: `id` (clave primaria), `libro_id` (clave ajena), `socio_id` (clave ajena), `fecha_prestamo`, `fecha_devolucion` (NULL mientras el préstamo siga activo).

## Funcionalidades

### Libros
- Añadir un libro.
- Mostrar todos los libros.
- Buscar libros por título o autor.
- Eliminar un libro que no tenga préstamos registrados.

### Socios
- Registrar un socio.
- Mostrar todos los socios.

### Préstamos
- Registrar un préstamo indicando el identificador del libro y del socio.
- Consultar los préstamos activos, mostrando título del libro y nombre del socio.
- Consultar el historial de préstamos de un socio.
- Registrar la devolución de un libro.

Al registrar un préstamo se comprobará que el libro y el socio existen y que el libro está disponible. Si el préstamo se registra correctamente, el libro pasará a estar no disponible.

Al registrar una devolución se rellenará `fecha_devolucion` y el libro volverá a estar disponible.

## Requisitos técnicos
- Python y MySQL.
- Conector `mysql-connector-python`.
- Consultas SQL parametrizadas.
- Separación entre conexión, operaciones de base de datos y menú.
- Gestión básica de errores y cierre correcto de cursores y conexiones.

## Entrega
1. Script SQL de creación de la base de datos y tablas.
2. Script SQL con datos iniciales.
3. Aplicación Python.
4. Demostración de un préstamo y su devolución.

La aplicación debe impedir que un libro se preste a dos socios simultáneamente.
