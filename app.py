import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado
st.header('Panel de anuncios de venta de vehículos')

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox para histograma
if st.checkbox('Mostrar histograma de precios'):
    st.write('Histograma del precio de los vehículos')
    fig = px.histogram(car_data, x="price", nbins=50, title="Distribución de precios")
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para diagrama de dispersión
if st.checkbox('Mostrar gráfico de dispersión Año vs Precio'):
    st.write('Dispersión de precio según el año del modelo')
    fig2 = px.scatter(car_data, x="model_year", y="price", title="Precio vs Año del modelo")
    st.plotly_chart(fig2, use_container_width=True)
