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
    #cuando se generan dinámicamente controles, se debe establecer un valor ky diferente para cada uno
    if col3.button("Añadir", key=f"add_{producto['id']}"):
        st.session_state.carrito.append(producto)

# Carrito de compra
st.subheader("Mi carrito")

if st.session_state.carrito:
    for producto in st.session_state.carrito:
        col1, col2, col3 = st.columns([3, 1, 1])

        col1.write(producto["nombre"])
        col2.write(f'{producto["precio"]} €')

        if col3.button("Eliminar", key=f"del_{producto['id']}"):
            st.session_state.carrito.remove(producto)
            st.rerun()

    total = sum(p["precio"] for p in st.session_state.carrito)
    st.write(f"**Total: {total} €**")
else:
    st.info("El carrito está vacío.")