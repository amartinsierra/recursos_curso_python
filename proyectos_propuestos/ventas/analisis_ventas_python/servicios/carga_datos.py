from pathlib import Path
import pandas as pd

COLUMNAS_OBLIGATORIAS = [
    "id_venta", "fecha", "cliente", "producto", "categoria", "unidades",
    "precio_unitario", "coste_unitario", "descuento", "region", "vendedor",
    "metodo_pago"
]

def cargar_datos(ruta=None):
    """Carga el CSV. Las fechas y columnas numéricas se validan en limpieza.py."""
    if ruta is None:
        ruta = Path(__file__).resolve().parents[1] / "datos" / "ventas.csv"
    df = pd.read_csv(ruta)
    faltan = set(COLUMNAS_OBLIGATORIAS) - set(df.columns)
    if faltan:
        raise ValueError(f"Faltan columnas obligatorias: {', '.join(sorted(faltan))}")
    return df
