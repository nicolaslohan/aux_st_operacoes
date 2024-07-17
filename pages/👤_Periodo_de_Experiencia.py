import streamlit as st
import pandas as pd

st.set_page_config(page_title="Perído de Experiência", page_icon=":bust_in_silhouette:")
st.write("Período de Experiência")

st.sidebar.header("Período de Experiência")
st.sidebar.write("Faça o upload do arquivo de período de experiência")

uploaded_files = st.sidebar.file_uploader("Escolhar arquivos XLSX", accept_multiple_files=False, type="xlsx")
