USE biblioteca;
INSERT INTO libros (titulo, autor, anyo, disponible) VALUES
('Cien años de soledad', 'Gabriel García Márquez', 1967, TRUE),
('La sombra del viento', 'Carlos Ruiz Zafón', 2001, TRUE),
('El nombre de la rosa', 'Umberto Eco', 1980, TRUE),
('1984', 'George Orwell', 1949, TRUE),
('Clean Code', 'Robert C. Martin', 2008, TRUE),
('Python Crash Course', 'Eric Matthes', 2019, TRUE),
('El Hobbit', 'J. R. R. Tolkien', 1937, TRUE),
('Fahrenheit 451', 'Ray Bradbury', 1953, TRUE);

INSERT INTO socios (nombre, email) VALUES
('Ana Martín', 'ana@example.com'),
('Luis Gómez', 'luis@example.com'),
('Marta Ruiz', 'marta@example.com'),
('Carlos Pérez', 'carlos@example.com');

INSERT INTO prestamos (libro_id, socio_id, fecha_prestamo, fecha_devolucion) VALUES
(1, 1, '2026-10-01', '2026-10-15'),
(5, 2, '2026-10-05', '2026-10-20');
