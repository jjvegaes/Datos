#%%
import streamlit as st
from os import listdir
#%%
# Crear boton desplegable para seleccionar el archivo a descargar
st.title("Descargar datos", )
st.markdown("Selecciona el archivo a descargar")
files = listdir(".")
# Solo los que acaban en .csv
files = [f for f in files if f.endswith(".csv")]
# Ordenar alfabeticamente
files = sorted(files)
#st.text(files)
# Crear boton desplegable
file = st.selectbox("Archivo", files)
# Crear boton para descargar
st.download_button(label="Descargar", data=open(file, "rb").read(), file_name=file, mime="text/csv")

# %%
