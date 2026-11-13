# Notas para el profesor

## Resultado de la limpieza de referencia
- Registros originales: 50
- Duplicados exactos eliminados: 2
- Fechas inválidas eliminadas: 1
- Filas con datos ausentes eliminadas: 3
- Filas con valores fuera de rango eliminadas: 2
- Registros finales: 42

Los recuentos de filas con datos ausentes y valores fuera de rango se realizan después de quitar duplicados y fechas inválidas. Una fila puede cumplir más de una condición según el orden de validación.

## Detección IQR
- Límite inferior de importe neto: -1042.38
- Límite superior de importe neto: 2052.62
- Número de anomalías de importe neto: 5

## Observaciones didácticas
- El CSV tiene exactamente 50 filas: 48 registros generados y dos duplicados exactos.
- La política de limpieza de la solución es una decisión de referencia, no la única posible. Se puede aceptar otra política si está justificada y se aplica coherentemente.
- El promedio de márgenes por venta no es lo mismo que el margen global (beneficio total / facturación total). Conviene pedir a los alumnos que distingan ambas métricas.
- La identificación IQR es estadística: un valor atípico no equivale necesariamente a un error.
