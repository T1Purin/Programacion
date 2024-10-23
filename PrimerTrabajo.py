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
st.link_button("Go", "https://www.google.com/search?q=cinnamoroll&client=ms-android-samsung-ss&sca_esv=60483cdc6baef8bd&udm=2&biw=360&bih=649&sxsrf=ADLYWIIbZOViADMRSsxF8vUfelksTkyyXA%3A1729678930051&ei=Us4YZ_fnArX75OUPkvnEqAU&oq=cinnamo&gs_lp=EhJtb2JpbGUtZ3dzLXdpei1pbWciB2Npbm5hbW8qAggDMgQQIxgnMgQQIxgnMgQQIxgnMg0QABiABBixAxhDGIoFMg0QABiABBixAxhDGIoFSPIRUOEFWIMHcAB4AJABAJgBV6AB6QGqAQEzuAEByAEA-AEBmAIDoAL-AcICCBAAGIAEGLEDwgIKEAAYgAQYQxiKBZgDAIgGAZIHATOgB4ET&sclient=mobile-gws-wiz-img")

#Barra lateral
st.sidebar.header('Mi primera barra lateral de streamlit')
st.sidebar.subheader('¡Hola,Barra Lateral!')
st.sidebar.write('Esto es una barra lateral')
st.sidebar.image('images.png')
st.sidebar.button('Haz click pero en la barra lateral')
txb = st.sidebar.text_input('Escriba algo en la barra:')
st.sidebar.write(f'Escribiste en la barra: {txb}')
