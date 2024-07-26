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

    def conditions(x):
        
        if x == 'Euclides da Cunha': return 'REGIONAL FILADÉLFIA'
        if x == 'Filadélfia': return 'REGIONAL FILADÉLFIA'
        if x == 'Itiúba': return 'REGIONAL FILADÉLFIA'
        if x == 'Queimadas': return 'REGIONAL FILADÉLFIA'
        if x == 'Caldeirão Grande': return 'REGIONAL FILADÉLFIA'
        if x == 'Ponto Novo': return 'REGIONAL FILADÉLFIA'
        if x == 'Saúde': return 'REGIONAL FILADÉLFIA'
        if x == 'Capim Grosso': return 'REGIONAL JACOBINA'
        if x == 'Quixabeira': return 'REGIONAL JACOBINA'
        if x == 'São José do Jacuípe': return 'REGIONAL JACOBINA'
        if x == 'Andorinha': return 'REGIONAL SENHOR DO BONFIM'
        if x == 'Campo Formoso': return 'REGIONAL SENHOR DO BONFIM'
        if x == 'Senhor do Bonfim': return 'REGIONAL SENHOR DO BONFIM'
        if x == 'Irecê': return 'REGIONAL JACOBINA'
        if x == 'Jacobina': return 'REGIONAL JACOBINA'
        if x == 'Caém': return 'REGIONAL FILADÉLFIA'
        if x == 'Pindobaçu': return 'REGIONAL FILADÉLFIA'
        if x == 'Cansanção': return 'REGIONAL FILADÉLFIA'
        if x == 'Antônio Gonçalves': return 'REGIONAL FILADÉLFIA'
        
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