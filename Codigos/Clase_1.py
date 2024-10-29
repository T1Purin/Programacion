import streamlit as st

def c1():
  #Cuerpo
  st.header('Mi primera aplicación de streamlit')
  st.subheader('¡Hola,Streamlit!')
  st.write('Esta es una aplicación simple')
  st.image('Archivos/images.png')
  st.button('Haz click')
  tx = st.text_input('Escriba algo:')
  st.write(f'Escribiste: {tx}')

  st.sidebar.header('Mi primera barra lateral de streamlit')
  st.sidebar.subheader('¡Hola, Barra Lateral!')
  st.sidebar.write('Esto es una barra lateral')
  st.image('Archivos/images.png')


