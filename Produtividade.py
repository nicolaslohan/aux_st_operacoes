import streamlit as st
import pandas as pd
from google.cloud import bigquery as bq
from google.oauth2 import service_account
from google import auth

st.set_page_config(page_title="Perído de Experiência", page_icon=":bust_in_silhouette:")
st.title("Produtividade - Operações")

st.sidebar.header("Período de Experiência")
st.sidebar.write("Faça o upload do arquivo de período de experiência")

uploaded_files = st.sidebar.file_uploader("Escolhar arquivos XLSX", accept_multiple_files=False, type="xlsx")

def data():
    credentials = service_account.Credentials.from_service_account_file('cred_bq/credentials_bq.json')
    scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])
    client = bq.Client(credentials=credentials)

    query = """
        SELECT * FROM `proxxima-data-429121.produtividade.unidade_colaboradores`
    """
    
    rows = client.query_and_wait(query)
    data = []
    for row in rows:
        r = {}
        for idx in range(len(row)):
            r[list(row.keys())[idx]] = row[idx]
        data.append(r)
    return data

st.write(pd.DataFrame(data()))