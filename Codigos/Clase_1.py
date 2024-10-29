import streamlit as st

def run():
  #Cuerpo
  st.header('Mi primera aplicación de streamlit')
  st.subheader('¡Hola,Streamlit!')
  st.write('Esta es una aplicación simple')
  st.image('Archivos/images.png')
  st.button('Haz click')
  tx = st.text_input('Escriba algo:')
  st.write(f'Escribiste: {tx}')

  st.sidebar.header('Mi primera barra lateral de streamlit')
  st.subheader('¡Hola barralateral,Streamlit!')


