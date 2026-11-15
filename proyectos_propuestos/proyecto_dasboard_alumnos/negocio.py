import polars as pl


def cargar_datos():
    alumnos = pl.read_csv("alumnos.csv")
    notas = pl.read_csv("notas.csv")

    return alumnos, notas
def obtener_notas_completas(alumnos, notas):
    datos = notas.join(
        alumnos,
        on="id_alumno",
        how="inner"
    )

    return datos

def filtrar_notas(datos, curso, asignatura, evaluacion, grupo):

    resultado = datos

    if curso != "Todos":
        resultado = resultado.filter(
            pl.col("curso") == curso
        )

    if asignatura != "Todas":
        resultado = resultado.filter(
            pl.col("asignatura") == asignatura
        )

    if evaluacion != "Todas":
        resultado = resultado.filter(
            pl.col("evaluacion") == evaluacion
        )

    if grupo != "Todos":
        resultado = resultado.filter(
            pl.col("grupo") == grupo
        )

    return resultado

def obtener_indicadores(datos):

    indicadores = datos.select(
        pl.col("id_alumno").n_unique().alias("alumnos"),
        pl.col("nota").mean().alias("media"),
        pl.col("nota").max().alias("maxima"),
        pl.col("nota").min().alias("minima"),
        (pl.col("nota") >= 5)
            .cast(pl.Float64)
            .mean()
            .mul(100)
            .alias("porcentaje_aprobados")
    )

    return indicadores.row(0, named=True)

def obtener_estadisticas_asignaturas(datos):

    resultado = datos.group_by("asignatura").agg(
        pl.col("id_alumno").n_unique().alias("alumnos_evaluados"),
        pl.col("nota").mean().round(2).alias("nota_media"),
        pl.col("nota").max().alias("nota_maxima"),
        (
            (pl.col("nota") >= 5)
            .cast(pl.Float64)
            .mean() * 100
        ).round(2).alias("porcentaje_aprobados")
    )

    return resultado.sort(
        "nota_media",
        descending=True
    )

def obtener_estadisticas_alumnos(datos):

    por_asignatura = datos.group_by(
        ["id_alumno", "nombre", "curso", "grupo", "asignatura"]
    ).agg(
        pl.col("nota").mean().alias("media_asignatura")
    )

    resultado = por_asignatura.group_by(
        ["id_alumno", "nombre", "curso", "grupo"]
    ).agg(
        pl.col("media_asignatura").mean().round(2).alias("nota_media"),

        pl.len().alias("asignaturas_evaluadas"),

        (
            (pl.col("media_asignatura") >= 5)
            .cast(pl.Int64)
            .sum()
        ).alias("asignaturas_aprobadas")
    )

    return resultado.sort(
        "nota_media",
        descending=True
    )

def obtener_evolucion_evaluaciones(datos, curso, asignatura, grupo):

    resultado = datos

    if curso != "Todos":
        resultado = resultado.filter(
            pl.col("curso") == curso
        )

    if asignatura != "Todas":
        resultado = resultado.filter(
            pl.col("asignatura") == asignatura
        )

    if grupo != "Todos":
        resultado = resultado.filter(
            pl.col("grupo") == grupo
        )

    return (
        resultado
        .group_by("evaluacion")
        .agg(
            pl.col("nota").mean().round(2).alias("nota_media")
        )
        .sort("evaluacion")
    )