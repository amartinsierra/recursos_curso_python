Ejercicio: Dashboard de análisis del rendimiento académico
1. Enunciado
Un centro de formación quiere desarrollar una aplicación que permita analizar los resultados académicos de sus alumnos.

Actualmente dispone de dos ficheros CSV:
- alumnos.csv: contiene información personal y académica de los alumnos.
- notas.csv: contiene las calificaciones obtenidas por los alumnos en diferentes asignaturas y evaluaciones.
Se pide desarrollar una aplicación utilizando Polars, Matplotlib y Streamlit que permita combinar ambos ficheros y analizar el rendimiento académico.

La aplicación permitirá seleccionar un curso, una asignatura y un periodo de evaluación, mostrando indicadores estadísticos, tablas y gráficos.

Requisitos funcionales
A. Filtros
La aplicación permitirá seleccionar:
- Curso: todos o cada uno de los cursos existentes.
- Asignatura: todas o una asignatura concreta.
- Evaluación: todas, primera o segunda.
- Grupo: todos o cada uno de los grupos existentes.
B. Indicadores estadísticos
Se mostrarán mediante st.metric():
Indicador	Descripción
Alumnos evaluados	Número de alumnos distintos con calificaciones
Nota media	Media de todas las calificaciones
Nota máxima	Mejor calificación
Nota mínima	Peor calificación
Porcentaje de aprobados	Porcentaje de notas iguales o superiores a 5

C. Análisis por asignatura
Mostrar una tabla con:
- Nombre de la asignatura.
- Número de alumnos evaluados.
- Nota media.
- Nota máxima.
- Porcentaje de aprobados.
Ordenar la tabla de mayor a menor nota media.
D. Análisis por alumno
Mostrar una tabla con:
- Nombre del alumno.
- Curso.
- Grupo.
- Nota media.
- Número de asignaturas evaluadas.
- Número de asignaturas aprobadas.
E. Gráficos con Matplotlib
Se deberán generar tres gráficos:
1. Nota media por asignatura: gráfico de barras para comparar el rendimiento en las diferentes asignaturas.
2. Evolución de las notas: gráfico de líneas que compare la nota media de la primera y segunda evaluación.
3. Distribución de calificaciones: histograma que permita observar cómo se distribuyen las notas obtenidas.