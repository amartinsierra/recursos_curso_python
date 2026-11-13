import streamlit as st

productos = [
    {"id": 1, "nombre": "Portátil", "precio": 800},
    {"id": 2, "nombre": "Ratón", "precio": 25},
    {"id": 3, "nombre": "Teclado", "precio": 45}
]

# Inicializar el carrito
if "carrito" not in st.session_state:
    st.session_state.carrito = []

st.title("Tienda online")

# Cabecera de la tabla
col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

col1.write("**Producto**")
col2.write("**Precio**")
col3.write("**Añadir**")
col4.write("**Eliminar**")

# Mostrar productos
for producto in productos:

    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

    col1.write(producto["nombre"])
    col2.write(f'{producto["precio"]} €')

    if col3.button("Añadir", key=f"add_{producto['id']}"):
        if producto not in st.session_state.carrito:
            st.session_state.carrito.append(producto)

    if col4.button("Eliminar", key=f"del_{producto['id']}"):
        if producto in st.session_state.carrito:
            st.session_state.carrito.remove(producto)

# Mostrar carrito
st.subheader("Mi carrito")

for producto in st.session_state.carrito:
    st.write(producto["nombre"], producto["precio"])