import pandas as pd
import numpy as np

COLUMNAS_NUMERICAS = ["unidades", "precio_unitario", "coste_unitario", "descuento"]

def limpiar_datos(df):
    """
    Devuelve (datos_limpios, informe).
    Política aplicada:
    - Elimina duplicados exactos.
    - Convierte fechas inválidas en NaT y elimina esas filas.
    - Convierte columnas numéricas; los valores no convertibles pasan a NaN.
    - Elimina filas sin identificador, cliente, producto o región.
    - Elimina filas con valores numéricos ausentes o fuera de dominio.
    - No elimina ventas atípicas válidas: se detectan en otro módulo.
    """
    informe = {}
    informe["registros_originales"] = len(df)

    trabajo = df.copy()
    duplicados = int(trabajo.duplicated().sum())
    trabajo = trabajo.drop_duplicates()
    informe["duplicados_eliminados"] = duplicados

    trabajo["fecha"] = pd.to_datetime(trabajo["fecha"], errors="coerce", dayfirst=True)
    fechas_invalidas = int(trabajo["fecha"].isna().sum())
    trabajo = trabajo.dropna(subset=["fecha"])
    informe["fechas_invalidas_eliminadas"] = fechas_invalidas

    for columna in COLUMNAS_NUMERICAS:
        trabajo[columna] = pd.to_numeric(trabajo[columna], errors="coerce")

    # Campos de identificación imprescindibles
    campos_texto = ["id_venta", "cliente", "producto", "categoria", "region", "vendedor", "metodo_pago"]
    nulos_antes = int(trabajo[campos_texto + COLUMNAS_NUMERICAS].isna().any(axis=1).sum())
    trabajo = trabajo.dropna(subset=campos_texto + COLUMNAS_NUMERICAS)

    # Reglas de negocio
    invalidos = (
        (trabajo["unidades"] <= 0) |
        (trabajo["precio_unitario"] <= 0) |
        (trabajo["coste_unitario"] < 0) |
        (trabajo["descuento"] < 0) |
        (trabajo["descuento"] > 100)
    )
    informe["filas_con_datos_ausentes_eliminadas"] = nulos_antes
    informe["filas_con_valores_fuera_de_rango_eliminadas"] = int(invalidos.sum())
    trabajo = trabajo.loc[~invalidos].copy()

    trabajo["unidades"] = trabajo["unidades"].astype(int)
    trabajo["importe_bruto"] = trabajo["unidades"] * trabajo["precio_unitario"]
    trabajo["importe_neto"] = trabajo["importe_bruto"] * (1 - trabajo["descuento"] / 100)
    trabajo["coste_total"] = trabajo["unidades"] * trabajo["coste_unitario"]
    trabajo["beneficio"] = trabajo["importe_neto"] - trabajo["coste_total"]
    trabajo["margen_pct"] = np.where(
        trabajo["importe_neto"] != 0,
        trabajo["beneficio"] / trabajo["importe_neto"] * 100,
        np.nan
    )

    informe["registros_finales"] = len(trabajo)
    informe["registros_descartados_total"] = informe["registros_originales"] - len(trabajo)
    return trabajo.reset_index(drop=True), informe
