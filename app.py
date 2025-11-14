import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')

st.header('PROYECTO DEL SPRINT 7: "Análisis de datos sobre la venta de vehículos"')
st.write('Se muestran nuestras primeras filas de nuestro conjunto de datos:')
st.dataframe(car_data.head(15))

start_button = st.button('Crear histograma')

if start_button:
    st.write(
        'Creación de un histograma del conjunto de datos de anuncios de venta de un automoviles')
    fig = px.histogram(car_data, x='model_year')
    st.plotly_chart(fig, use_container_width=True)


dispercion_button = st.button('Crear gráfica de disperción')

if dispercion_button:
    st.write('Al presionar este boton creamos un gráfico de disperción sobre el conjunto de datos de anuncios de venta de automoviles')
    fig_1 = px.scatter(car_data, x='model_year')
    st.plotly_chart(fig_1, use_container_width=True)
