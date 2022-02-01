import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import power_transform
from sklearn.cluster import KMeans

st.header("Classificação de Clientes Olist")

st.subheader("Insira os dados para a classificação")

def get_history_data():
    data = pd.read_csv('rfm_dataset.csv')
    data.set_index('customer_unique_id')
    return data


def get_user_data():
    frequency = st.sidebar.text_input("Frequência")
    recency = st.sidebar.text_input("Recência")
    monetary = st.sidebar.text_input("Monetário")
    
    user_data_dict = {'customer_unique_id':'user',
             'frequency': frequency,
             'recency': recency,
             'monetary': monetary}

    features = pd.DataFrame(user_data_dict, index=[0])
    features.set_index('customer_unique_id')
    
    return features

def transform_data(rfm, user_data):
    rfm.set_index('customer_unique_id', inplace = True)
    rfm.monetary = pd.to_numeric(rfm.monetary, downcast="float")
    Q1 = rfm.monetary.quantile(0.05)
    Q3 = rfm.monetary.quantile(0.95)
    IQR = Q3 - Q1
    rfm = rfm[(rfm.monetary >= Q1 - 1.5*IQR) & (rfm.monetary <= Q3 + 1.5*IQR)]
    initial_data = pd.concat([rfm,user_data])
    initial_data.set_index('customer_unique_id', inplace = True)
    #data_normalized = power_transform(initial_data)
    #minmax = MinMaxScaler()
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(initial_data)
    final_data_scaled = pd.DataFrame(data_scaled, initial_data.index, initial_data.columns)
    return final_data_scaled

def train_model(data_input):
    kmeans = KMeans(n_clusters=3, init='k-means++',max_iter=300, random_state=1)
    kmeans.fit(data_input)
    print(kmeans.labels_)
    data_input['cluster'] = kmeans.labels_
    return data_input['cluster'].loc['user']
    
user_dataset = get_user_data()
history_dataset = get_history_data()
if st.sidebar.button("Classificar"):
    transformed_data = transform_data(history_dataset, user_dataset)
    print(type(transformed_data))
    prediction = train_model(transformed_data)
    if prediction == 0:
        st.write("Parabéns, você é um cliente Prata")
    elif prediction == 1:
        st.write("Parabéns, você é um cliente Ouro")
    else:
        st.write("Parabéns, você é um cliente Bronze")
else:
    st.write('Aguardando Dados')






