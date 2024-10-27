import pandas as pd
import streamlit as st

d1 = pd.read_csv('Archivos/AlarmasSistema.csv', sep=';')
st.write('Lectura de archivos')
st.write(d1.head())
st.image('Archivos/0-0-jojos-bizarre-adventure-glosario-diccionario-terminos.webp')
