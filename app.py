import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Analisis de venta de vehiculos usados")

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
     
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_lineplot=st.checkbox("Construir la relacion de los cilindros")

if build_lineplot:
    st.write("Relacion entre la condicion y los cilindros del vehiculo por transmision")
    df_car=car_data.groupby(["transmission", "condition"])["cylinders"].mean().reset_index()
    fig_2=px.line(df_car, x="condition", y="cylinders", color="transmission", title="Relacion de los cilindros y la condicion del vehiculo")
    st.plotly_chart(fig_2, use_container_width=True)