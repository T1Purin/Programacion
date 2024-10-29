import streamlit as st

if st.button("Home"):
    st.sidebar.switch_Codigos("app.py")
if st.button("Page 1"):
    st.sidebar.switch_Codigos("Archivos/Clase_1.py")
if st.button("Page 2"):
    st.sidebar.switch_Codigos("Archivos/Clase_2.py")
  
