import streamlit as st

from datetime import date

import consumos as dao


st.set_page_config(
    page_title="Consumo energético",
    page_icon="⚡"
)

st.title("⚡ Registro de consumo energético")

opcion = st.sidebar.radio(
    "Menú",
    ["Registrar consumo", "Consultar consumos", "Eliminar consumo"]
)


# REGISTRAR CONSUMO

if opcion == "Registrar consumo":

    st.header("Nueva lectura")

    with st.form("form_consumo"):

        instalacion = st.text_input("Nombre de la instalación")

        fecha = st.date_input(
            "Fecha de lectura",
            value=date.today(),
            max_value=date.today()
        )

        cantidad = st.number_input(
            "Consumo (kWh)",
            min_value=0.0,
            step=0.1
        )

        observaciones = st.text_area("Observaciones")

        enviado = st.form_submit_button("Guardar")

        if enviado:

            if not instalacion.strip() or cantidad <= 0:
                st.error("Introduce una instalación y un consumo válido")

            else:

                dao.insertar_consumo(
                    instalacion,
                    fecha,
                    cantidad,
                    observaciones
                )

                st.success("Lectura registrada")


# CONSULTAR CONSUMOS

elif opcion == "Consultar consumos":

    st.header("Consulta de lecturas")

    instalacion = st.text_input("Filtrar por instalación")

    col1, col2 = st.columns(2)

    with col1:
        fecha_inicio = st.date_input(
            "Desde",
            value=date(date.today().year, 1, 1)
        )

    with col2:
        fecha_fin = st.date_input(
            "Hasta",
            value=date.today()
        )

    if st.button("Buscar"):

        if fecha_inicio > fecha_fin:
            st.error("El periodo de fechas no es válido")

        else:

            resultado = dao.buscar_consumos(
                instalacion,
                fecha_inicio,
                fecha_fin
            )

            if resultado:

                total = sum(
                    r["consumo_kwh"] for r in resultado
                )

                st.metric("Consumo total", f"{total:.2f} kWh")

                for lectura in resultado:

                    st.write(
                        f"**{lectura['instalacion']}** — "
                        f"{lectura['fecha'].date()} — "
                        f"{lectura['consumo_kwh']} kWh"
                    )

                    if lectura["observaciones"]:
                        st.caption(lectura["observaciones"])

                    st.divider()

            else:
                st.info("No se encontraron lecturas")


# ELIMINAR CONSUMOS

elif opcion == "Eliminar consumo":

    st.header("Eliminar lectura")

    resultado = dao.listar_consumos()

    if resultado:

        seleccion = st.selectbox(
            "Selecciona una lectura",
            resultado,
            format_func=lambda r: (
                f"{r['instalacion']} - "
                f"{r['fecha'].date()} - "
                f"{r['consumo_kwh']} kWh"
            )
        )

        if st.button("Eliminar"):

            dao.eliminar_consumo(seleccion["_id"])

            st.success("Lectura eliminada")

            st.rerun()

    else:
        st.info("No hay lecturas registradas")