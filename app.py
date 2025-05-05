import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Mi Aplicación Streamlit",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="auto"
)

# Título principal
st.title("Mi Aplicación Streamlit")

# Sidebar
with st.sidebar:
    st.header("Configuración")
    nombre = st.text_input("Tu nombre")
    color = st.color_picker("Elige un color", "#0066ff")
    
# Contenido principal
st.header("¡Bienvenido a Streamlit!")

if nombre:
    st.markdown(f"### Hola, {nombre}! 👋")
    st.write(f"Tu color elegido es: {color}")
    
    # Demostración de algunos widgets
    tab1, tab2, tab3 = st.tabs(["Datos", "Visualización", "Acerca de"])
    
    with tab1:
        st.subheader("Ejemplo de tabla de datos")
        st.dataframe({
            "Columna 1": [1, 2, 3, 4],
            "Columna 2": [10, 20, 30, 40],
            "Columna 3": ["a", "b", "c", "d"]
        })
        
    with tab2:
        st.subheader("Ejemplo de gráfico")
        st.line_chart({"datos": [1, 5, 2, 6, 2, 8, 3]})
        
    with tab3:
        st.subheader("Acerca de esta aplicación")
        st.info("Esta es una aplicación de demostración creada con Streamlit y UV.")
        with st.expander("Ver más información"):
            st.write("""
                Streamlit es una biblioteca de Python que facilita la creación de aplicaciones web 
                para ciencia de datos y machine learning en minutos.
                
                Esta app fue creada automáticamente con el script streamlit-uv.py.
            """)
else:
    st.info("👈 Ingresa tu nombre en la barra lateral para comenzar")

# Pie de página
st.divider()
st.caption("Creado con Streamlit y UV 🚀")
