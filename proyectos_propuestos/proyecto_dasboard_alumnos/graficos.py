import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


def grafico_notas_asignaturas(datos):

    plt.bar(
        datos["asignatura"].to_list(),
        datos["nota_media"].to_list()
    )

    plt.title("Nota media por asignatura")
    plt.xlabel("Asignatura")
    plt.ylabel("Nota media")

    plt.ylim(0, 10)
    plt.grid(axis="y", alpha=0.3)




def grafico_evolucion_evaluaciones(datos):

    plt.plot(
        datos["evaluacion"].to_list(),
        datos["nota_media"].to_list(),
        marker="o"
    )

    plt.title("Evolución de las notas")
    plt.xlabel("Evaluación")
    plt.ylabel("Nota media")

    plt.xticks(datos["evaluacion"].to_list())
    plt.ylim(0, 10)

    plt.grid(alpha=0.3)




def grafico_distribucion_notas(datos):

    plt.hist(
        datos["nota"].to_list(),
        bins=10,
        range=(0, 10),
        edgecolor="black"
    )

    plt.title("Distribución de calificaciones")
    plt.xlabel("Nota")
    plt.ylabel("Número de calificaciones")

    plt.xticks(range(0, 11))
    plt.grid(axis="y", alpha=0.3)

