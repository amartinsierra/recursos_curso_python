import streamlit as st

productos = [
    {"id": 1, "nombre": "Portátil", "precio": 800},
    {"id": 2, "nombre": "Ratón", "precio": 25},
    {"id": 3, "nombre": "Teclado", "precio": 45}
]

if "carrito" not in st.session_state:
    st.session_state.carrito = []

st.title("Tienda online")

# Catálogo de productos
st.subheader("Productos disponibles")

for producto in productos:
    col1, col2, col3 = st.columns([3, 1, 1])

    col1.write(producto["nombre"])
    col2.write(f'{producto["precio"]} €')

    if col3.button("Añadir", key=f"add_{producto['id']}"):

        # Buscar si el producto ya está en el carrito
        encontrado = False

        for item in st.session_state.carrito:
            if item["id"] == producto["id"]:
                item["cantidad"] += 1
                encontrado = True
                break

        # Si no existe, lo añadimos con cantidad 1
        if not encontrado:
            nuevo_item = producto.copy()
            nuevo_item["cantidad"] = 1
            st.session_state.carrito.append(nuevo_item)

# Carrito de compra
st.subheader("Mi carrito")

if st.session_state.carrito:

    for item in st.session_state.carrito:
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

        col1.write(item["nombre"])
        col2.write(f'{item["precio"]} €')
        col3.write(f'Unidades: {item["cantidad"]}')

        if col4.button("Eliminar", key=f"del_{item['id']}"):
            st.session_state.carrito.remove(item)
            st.rerun()

    total = sum(
        item["precio"] * item["cantidad"]
        for item in st.session_state.carrito
    )

    st.write(f"**Total: {total} €**")

else:
    st.info("El carrito está vacío.")