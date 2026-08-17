import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Análisis de vehículos en venta')

if st.button('Mostrar histograma de precios'):
    st.write('Distribución de precios de los vehículos')
    fig = px.histogram(df, x='price', title='Distribución de precios')
    st.plotly_chart(fig)

if st.button('Mostrar gráfico de dispersión'):
    st.write('Relación entre odómetro y precio')
    fig = px.scatter(df, x='odometer', y='price', title='Odómetro vs Precio')
    st.plotly_chart(fig)
