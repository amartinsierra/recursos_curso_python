# Ejercicio: Sistema de análisis y visualización de ventas

Una empresa comercializadora de productos tecnológicos necesita una aplicación para analizar sus ventas. Debes desarrollar una solución con Python, Pandas, NumPy y Streamlit.

## Datos
Utiliza `datos/ventas.csv`. Contiene 50 registros y puede incluir datos duplicados, ausentes, fechas incorrectas y valores numéricos no válidos. No presupongas que todos los registros son correctos.

## Requisitos

1. **Carga y limpieza**
   - Cargar el CSV con Pandas.
   - Informar del número de registros, nulos y duplicados.
   - Convertir fechas y columnas numéricas.
   - Definir y aplicar reglas de validación.
   - Justificar qué registros se eliminan y por qué.
   - Calcular importe bruto, importe neto, coste total, beneficio y margen.

2. **Resumen**
   - Mostrar facturación, beneficio, número de ventas, unidades, ticket medio y margen medio.
   - Mostrar evolución mensual de facturación y beneficio.
   - Comparar facturación por región y categoría.

3. **Productos**
   - Ranking de diez productos por facturación y por beneficio.
   - Productos con menor margen.
   - Gráfico de unidades vendidas frente a beneficio.
   - Filtro por categoría.

4. **Clientes y regiones**
   - Compras, importe, beneficio y ticket medio por cliente.
   - Diez clientes con mayor compra y mayor beneficio.
   - Facturación, beneficio, ventas y porcentaje de facturación por región.

5. **Anomalías**
   - Utilizar NumPy para calcular Q1, Q3 e IQR.
   - Aplicar los límites Q1 - 1,5*IQR y Q3 + 1,5*IQR.
   - Mostrar los registros anómalos sin eliminarlos automáticamente.

6. **Filtros**
   - Periodo de fechas, categoría, región, vendedor y método de pago.
   - Todos los indicadores y gráficos deben respetar los filtros.

7. **Calidad del código**
   - Separar interfaz y lógica de negocio.
   - Utilizar funciones reutilizables.
   - Evitar repetir cálculos.
   - Mantener una estructura de proyecto ordenada.

## Ampliaciones opcionales
- Comparar dos periodos y calcular variaciones porcentuales.
- Segmentar clientes mediante percentiles.
- Exportar los datos filtrados y las anomalías mediante `st.download_button`.
- Añadir una explicación de tres conclusiones empresariales basadas en los resultados.

## Entrega
Entregar el proyecto Python completo, el CSV utilizado y una breve explicación de las decisiones de limpieza y de tres conclusiones obtenidas del análisis.
