import pandas as pd
import matplotlib.pyplot as plt 
import streamlit as st

#Cuerpo
st.header('Mi primera aplicación de streamlit')
st.subheader('¡Hola,Streamlit!')
st.write('Esta es una aplicación simple')
st.image('images.png')
st.button('Haz click')
tx = st.text_input('Escriba algo:')
st.write(f'Escribiste: {tx}')

#Barra lateral
st.sidebar.header('Mi primera barra lateral de streamlit')
st.sidebar.subheader('¡Hola,Barra Lateral!')
st.write('Esto es una barra lateral')
st.image('images.png')
st.button('Haz click pero en la barra lateral')
txb = st.text_imput('Escriba algo en la barra:')
st.write(f'Escribiste en la barra: {txb}')
