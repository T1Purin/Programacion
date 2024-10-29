import streamlit as st

# Títulos de las páginas
pages = {
    "Home": "home",
    "Page 1": "clase_1",
    "Page 2": "clase_2"
}

# Selector de página en la barra lateral
selection = st.sidebar.radio("Ir a:", list(pages.keys()))

# Mostrar la página seleccionada
if selection == "Home":
    import Codigos.Clase_0
    Codigos.Clase_0.c0()
    # Aquí puedes agregar más contenido para la página principal
elif selection == "Page 1":
    import Codigos.Clase_1  # Asegúrate de que la ruta sea correcta
    Codigos.Clase_1.c1()    # Asumiendo que tienes una función 'run' en Clase_1.py
elif selection == "Page 2":
    import Codigos.Clase_2  # Asegúrate de que la ruta sea correcta
    Codigos.Clase_2.c2()    # Asumiendo que tienes una función 'run' en Clase_2.py

