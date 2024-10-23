import pandas as pd
import matplotlib.pyplot as plt 
import streamlit as st

st.header('Mi primera aplicación de streamlit')
st.subheader('¡Hola,Streamlit!')
st.write('Esta es una aplicación simple')
st.image('images.png')
st.button('Dale click')
tx = st.text_input('Escriba algo')
st.write(f'Escribiste: {tx}')
st.checkbox('Seleccionar')
