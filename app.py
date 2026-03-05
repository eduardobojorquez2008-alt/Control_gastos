import streamlit as st
from database import inicializar_archivo, guardar_gasto, leer_gastos, eliminar_gasto
from datetime import date
st.set_page_config(page_title="Finanzas", page_icon="💳", layout="centered")
st.title("Control de gastos personales 💵")

inicializar_archivo()

st.header("Agregar gasto")

nombre = st.text_input("Nombre del gasto")
categoria = st.selectbox("Categoría", ["Comida", "Transporte", "Entretenimiento", "Otros"])
monto = st.number_input("Cantidad", min_value=0.0, format="%.2f")
fecha = st.date_input("Fecha", value=date.today())

if st.button("Agregar"):
    if nombre.strip() == "":
        st.warning("Escribe un nombre para el gasto.")
    elif monto <= 0:
        st.warning("Ingresa una cantidad válida.")
    else:
        guardar_gasto(nombre, categoria, monto, fecha)
        st.success(f"Gasto '{nombre}' agregado correctamente.")

st.header("Mis gastos")
df = leer_gastos()

if df.empty:
    st.info("No hay gastos registrados todavía.")
else:
    st.dataframe(df)
    total = df["Monto"].sum()
    st.metric("Total gastado", f"${total:,.2f}")

    st.subheader("Eliminar gasto")
    indice = st.number_input(
        "Número de fila a eliminar (ver tabla arriba)",
        min_value=0,
        max_value=len(df) - 1,
        step=1
    )
    if st.button("Eliminar"):
        eliminar_gasto(indice)
        st.success("Gasto eliminado correctamente.")

        st.rerun()


