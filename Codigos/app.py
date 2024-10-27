import pandas as pd
import streamlit as st

d1 = pd.read_csv('Archivos/AlarmasSistema.csv', sep=';')
st.write(d1.head())

