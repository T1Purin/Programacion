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
st.link_button("Go", "Cinnamoroll https://g.co/kgs/uWGXCVp")
st.write('hola'ñ

#Barra lateral
st.sidebar.header('Mi primera barra lateral de streamlit')
st.sidebar.subheader('¡Hola,Barra Lateral!')
st.sidebar.write('Esto es una barra lateral')
st.sidebar.image('images.png')
st.sidebar.button('Haz click pero en la barra lateral')
txb = st.sidebar.text_input('Escriba algo en la barra:')
st.sidebar.write(f'Escribiste en la barra: {txb}')
