import numpy as np
import pandas as pd

def calcular_kpis(df):
    if df.empty:
        return {
            "facturacion": 0.0, "beneficio": 0.0, "ventas": 0,
            "unidades": 0, "ticket_medio": 0.0, "margen_medio": 0.0
        }
    return {
        "facturacion": float(df["importe_neto"].sum()),
        "beneficio": float(df["beneficio"].sum()),
        "ventas": int(df["id_venta"].nunique()),
        "unidades": int(df["unidades"].sum()),
        "ticket_medio": float(df["importe_neto"].mean()),
        "margen_medio": float(df["margen_pct"].mean())
    }

def resumen_por_mes(df):
    resultado = df.copy()
    resultado["mes"] = resultado["fecha"].dt.to_period("M").astype(str)
    return resultado.groupby("mes", as_index=False).agg(
        facturacion=("importe_neto", "sum"),
        beneficio=("beneficio", "sum"),
        ventas=("id_venta", "nunique")
    ).sort_values("mes")

def ranking_productos(df):
    return df.groupby(["producto", "categoria"], as_index=False).agg(
        facturacion=("importe_neto", "sum"),
        beneficio=("beneficio", "sum"),
        unidades=("unidades", "sum"),
        margen_medio=("margen_pct", "mean")
    )

def ranking_clientes(df):
    return df.groupby("cliente", as_index=False).agg(
        compras=("id_venta", "nunique"),
        importe_total=("importe_neto", "sum"),
        beneficio=("beneficio", "sum"),
        ticket_medio=("importe_neto", "mean")
    )

def analisis_regiones(df):
    total = df["importe_neto"].sum()
    resultado = df.groupby("region", as_index=False).agg(
        facturacion=("importe_neto", "sum"),
        beneficio=("beneficio", "sum"),
        ventas=("id_venta", "nunique")
    )
    resultado["porcentaje_facturacion"] = np.where(
        total != 0, resultado["facturacion"] / total * 100, 0
    )
    return resultado.sort_values("facturacion", ascending=False)

def detectar_anomalias_iqr(df, columna="importe_neto"):
    """Devuelve ventas atípicas y límites IQR. No modifica ni elimina el DataFrame."""
    if df.empty:
        return df.copy(), np.nan, np.nan
    q1 = float(np.percentile(df[columna].dropna(), 25))
    q3 = float(np.percentile(df[columna].dropna(), 75))
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    anomalias = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    return anomalias, limite_inferior, limite_superior

def comparar_periodos(df, inicio_a, fin_a, inicio_b, fin_b):
    a = df[df["fecha"].between(pd.Timestamp(inicio_a), pd.Timestamp(fin_a))]
    b = df[df["fecha"].between(pd.Timestamp(inicio_b), pd.Timestamp(fin_b))]
    fact_a, fact_b = a["importe_neto"].sum(), b["importe_neto"].sum()
    beneficio_a, beneficio_b = a["beneficio"].sum(), b["beneficio"].sum()
    variacion = ((fact_b - fact_a) / abs(fact_a) * 100) if fact_a != 0 else np.nan
    return {
        "periodo_a_facturacion": float(fact_a),
        "periodo_b_facturacion": float(fact_b),
        "variacion_facturacion_pct": float(variacion) if not np.isnan(variacion) else np.nan,
        "periodo_a_beneficio": float(beneficio_a),
        "periodo_b_beneficio": float(beneficio_b)
    }
