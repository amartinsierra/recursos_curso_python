from datetime import datetime

from conexion import consumos


if consumos.count_documents({}) == 0:

    consumos.insert_many([
        {
            "instalacion": "Oficina central",
            "fecha": datetime(2026, 10, 1),
            "consumo_kwh": 450,
            "observaciones": "Consumo de octubre"
        },
        {
            "instalacion": "Oficina central",
            "fecha": datetime(2026, 11, 1),
            "consumo_kwh": 425,
            "observaciones": "Consumo de noviembre"
        },
        {
            "instalacion": "Vivienda norte",
            "fecha": datetime(2026, 10, 1),
            "consumo_kwh": 180,
            "observaciones": "Consumo de octubre"
        },
        {
            "instalacion": "Vivienda norte",
            "fecha": datetime(2026, 11, 1),
            "consumo_kwh": 250,
            "observaciones": "Consumo de noviembre"
        },
        {
            "instalacion": "Nave industrial",
            "fecha": datetime(2026, 10, 1),
            "consumo_kwh": 4200,
            "observaciones": "Consumo de octubre"
        }
    ])

    print("Datos iniciales insertados")

else:
    print("Ya existen datos")