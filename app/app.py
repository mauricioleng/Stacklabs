import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import power_transform
from sklearn.cluster import KMeans

st.write("Classificação de Clientes Olist")

st.subheader("Insira os dados para a classificação")

def get_history_data():
    data = pd.read_csv('.\\dataset\\rfm_dataset.csv')
    return data


def get_user_data():
    frequency = st.sidebar.text_input("Frequência")
    recency = st.sidebar.text_input("Recência")
    monetary = st.sidebar.text_input("Monetário")
    
    user_data = {'customer_unique_id':'user'
             'frequency': frequency,
             'recency': recency,
             'monetary': monetary}

    features = pd.DataFrame(user_data, index='customer_unique_id')

    return features

def transform_data(history_data, user_data):
    initial_data = history_data.append(user_data)
    data_normalized = power_transform(initial_data)
    minmax = MinMaxScaler()
    data_scaled = minmax.fit_transform(data_normalized)
    return data_scaled

def train_model(data):
    kmeans = KMeans(n_clusters=3, init='k-means++',max_iter=300)
    kmeans.fit(rfm )
    return prediction
    
user_data = get_user_data()
history_data = get_history_data()
if st.sidebar.button("Classificar"):
    transformed_data = transform_data(history_data, user_data)
    prediction = train_model(transformed_data)
    if prediction == 0:
        st.write("Parabéns, você é um cliente Bronze")
    elif prediction == 1:
        st.write("Parabéns, você é um cliente Prata")
    else:
        st.write("Parabéns, você é um cliente Ouro")
else:
    st.write('Aguardando Dados')






