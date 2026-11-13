from datetime import datetime

from conexion import consumos


def insertar_consumo(instalacion, fecha, cantidad, observaciones):

    documento = {
        "instalacion": instalacion,
        "fecha": datetime.combine(fecha, datetime.min.time()),
        "consumo_kwh": cantidad,
        "observaciones": observaciones
    }

    consumos.insert_one(documento)


def listar_consumos():
    return list(consumos.find().sort("fecha", -1))


def buscar_consumos(instalacion, fecha_inicio, fecha_fin):

    filtro = {
        "fecha": {
            "$gte": datetime.combine(
                fecha_inicio, datetime.min.time()
            ),
            "$lte": datetime.combine(
                fecha_fin, datetime.max.time()
            )
        }
    }

    if instalacion:
        filtro["instalacion"] = {
            "$regex": instalacion,
            "$options": "i"
        }

    return list(consumos.find(filtro).sort("fecha", -1))


def eliminar_consumo(id_consumo):
    consumos.delete_one({"_id": id_consumo})