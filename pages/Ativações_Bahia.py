import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Ativações Bahia", page_icon=":white_check_mark:")
st.title("Ativações Bahia")

st.sidebar.header("Ativações Bahia")
st.sidebar.write("Faça o upload do arquivo das solicitações fechadas produtivas, exportadas do Painel de Serviços do ANIEL.")

ativacoes = st.sidebar.file_uploader(
    "Escolha um arquivo", type="XLSX", accept_multiple_files=False
)

if ativacoes is not None:

    df = pd.read_excel(ativacoes)

    df.columns = df.iloc[0]
    df.drop(df.index[0], inplace=True)
    df["Cidade"] = df["Cidade"].map(str.strip).map(str.upper)

    def conditions(x):
        
        if x == 'EUCLIDES DA CUNHA': return 'REGIONAL FILADÉLFIA'
        if x == 'FILADÉLFIA': return 'REGIONAL FILADÉLFIA'
        if x == 'ITIÚBA': return 'REGIONAL FILADÉLFIA'
        if x == 'QUEIMADAS': return 'REGIONAL FILADÉLFIA'
        if x == 'CALDEIRÃO GRANDE': return 'REGIONAL FILADÉLFIA'
        if x == 'PONTO NOVO': return 'REGIONAL FILADÉLFIA'
        if x == 'SAÚDE': return 'REGIONAL FILADÉLFIA'
        if x == 'CAPIM GROSSO': return 'REGIONAL JACOBINA'
        if x == 'QUIXABEIRA': return 'REGIONAL JACOBINA'
        if x == 'SÃO JOSÉ DO JACUÍPE': return 'REGIONAL JACOBINA'
        if x == 'ANDORINHA': return 'REGIONAL SENHOR DO BONFIM'
        if x == 'CAMPO FORMOSO': return 'REGIONAL SENHOR DO BONFIM'
        if x == 'SENHOR DO BONFIM': return 'REGIONAL SENHOR DO BONFIM'
        if x == 'IRECÊ': return 'REGIONAL JACOBINA'
        if x == 'JACOBINA': return 'REGIONAL JACOBINA'
        if x == 'CAÉM': return 'REGIONAL FILADÉLFIA'
        if x == 'PINDOBAÇU': return 'REGIONAL FILADÉLFIA'
        if x == 'CANSANÇÃO': return 'REGIONAL FILADÉLFIA'
        if x == 'ANTÔNIO GONÇALVES': return 'REGIONAL FILADÉLFIA'
        
    func = np.vectorize(conditions)
    unidade = func(df["Cidade"])
    df["Unidade"] = unidade
    
    df["Data/Hora Encerramento"] = pd.to_datetime(df['Data/Hora Encerramento'], dayfirst=True, format='%d/%m/%Y %H:%M')
    df["Data/Hora Encerramento"] = df['Data/Hora Encerramento'].dt.date
    data = df["Data/Hora Encerramento"].unique()
    st.write(f'Data do fechamento: {data[0]}')
    
    filtro = df[["Nº. Ordem Serviço", "Unidade"]].pivot_table(index='Unidade', aggfunc=len, fill_value=0)

    #st.write(f'Data de fechamento: {date}')
    st.write(filtro)
    
    filtro2 = df[["Nº. Ordem Serviço", "Unidade", "Data/Hora Encerramento", "Cidade"]].pivot_table(index=['Data/Hora Encerramento', 'Nº. Ordem Serviço', 'Unidade', 'Cidade'], aggfunc=len, fill_value=0)
    st.write(filtro2)

else:
    st.warning('Faça upload do arquivo para visualizar.')