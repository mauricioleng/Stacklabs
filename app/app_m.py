import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Projeto Stack Labs')
st.subheader('**Agrupamento e Classificação de Clientes**')

data=pd.read_csv('app/olist.csv')

hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """


st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)





opcao_1 = st.sidebar.checkbox('Mostrar Data Frame')
if opcao_1:

    st.sidebar.markdown('## Filtro para a DataFrame')

    classes = list(data['class_k'].unique())
    classes.append('Todas')
    values=list(data['monetary'].unique())

    classe = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = classes)
    

    if classe != 'Todas':
        df_classe = data.query('class_k == @classe')
      
        st.write(df_classe)  
    else:
        st.write(data)
 




 
option = st.sidebar.selectbox(
     'Opçoes Promocionais',
     ('Cupons de desconto', 'Recomendação de Produtos', 'Envio de Ofertas','Programa de Fidelidade','Campanha Promocional'))

st.write('You selected:', option)

option = st.sidebar.selectbox(
     'Canais de Envio',
     ('Email', 'WhatsApp'))

st.write('You selected:', option)

result=st.sidebar.button('Enviar')
