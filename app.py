import streamlit as st

pages = {
    "Home": "home",
    "Page 1": "clase_1",
    "Page 2": "clase_2"
}

selection = st.sidebar.selectbox("Ir a:", list(pages.keys()))


if selection == "Home":
    import Codigos.Clase_0
    Codigos.Clase_0.c0()
elif selection == "Page 1":
    import Codigos.Clase_1  
    Codigos.Clase_1.c1()   
elif selection == "Page 2":
    import Codigos.Clase_2  
    Codigos.Clase_2.c2()   

