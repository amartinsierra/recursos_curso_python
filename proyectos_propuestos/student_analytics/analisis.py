import polars as pl


def crear_dataframe(registros):
    """Convierte la lista de diccionarios obtenida de MySQL en un DataFrame."""
    return pl.DataFrame(registros).with_columns(
        pl.col("fecha").cast(pl.Date),
        pl.col("nota").cast(pl.Float64),
    )


def obtener_indicadores(df):
    return df.select(
        pl.col("alumno").n_unique().alias("alumnos"),
        pl.len().alias("calificaciones"),
        pl.col("nota").mean().round(2).alias("media"),
        pl.col("nota").max().alias("maxima"),
        pl.col("nota").min().alias("minima"),
        (pl.col("nota") >= 5).sum().alias("aprobados"),
        (pl.col("nota") < 5).sum().alias("suspensos"),
    )


def medias_por_asignatura(df):
    return (
        df.group_by("asignatura")
        .agg(pl.col("nota").mean().round(2).alias("nota_media"))
        .sort("nota_media", descending=True)
    )


def distribucion_notas(df):
    return (
        df.with_columns(
            pl.when(pl.col("nota") < 5).then(pl.lit("Suspenso"))
            .when(pl.col("nota") < 7).then(pl.lit("Aprobado"))
            .when(pl.col("nota") < 9).then(pl.lit("Notable"))
            .otherwise(pl.lit("Sobresaliente"))
            .alias("intervalo")
        )
        .group_by("intervalo")
        .agg(pl.len().alias("cantidad"))
        .sort("intervalo")
    )
