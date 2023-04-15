#%%
import streamlit as st
from os import listdir
#%%
st.title("Descargar datos", )
st.markdown("Selecciona los datos a descargar")
files = listdir(".")
files = [f for f in files if f.endswith(".csv")]
files = sorted(files)
file = st.selectbox("Archivo", files)
st.download_button(label="Descargar", data=open(file, "rb").read(), file_name=file, mime="text/csv")

# %%
