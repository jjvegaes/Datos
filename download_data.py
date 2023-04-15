#%%
import streamlit as st
from os import listdir
import pandas as pd
#%%
files = listdir(".")
files = [f for f in files if f.endswith(".csv")]
files = sorted(files)
activos = ['AUDUSD', 'GBPUSD', 'EURUSD', 'Brent', 'Bitcoin', 'Dollar Index', 'S&P500', 'DAX Futuro','DAX Mini', 'Gold', 'Crudo', 'Nasdaq', 'News', 'Silver', 'Dow']
# Mapa de nombres - activos
st.write("## Mapa de nombres - activos")
st.markdown("Última actualización: 15-04-2023")
st.table(pd.DataFrame({"Archivo": files, "Activo": activos}))
st.title("Descargar datos")
st.markdown("Selecciona los datos a descargar")
file = st.selectbox("Archivo", files)
st.download_button(label="Descargar", data=open(file, "rb").read(), file_name=file, mime="text/csv")

# %%
