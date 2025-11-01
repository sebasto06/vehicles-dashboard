# importar librerías
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Título de la aplicación centrado
st.title('Anuncios de vehículos en EE.UU.')

# Leer los datos desde el archivo CSV vehicled_us_clean.csv
df = pd.read_csv('./vehicles_us_cleaned.csv')

# Mostrar los datos en la aplicación
st.write(df)

# Histograma de los tipos de vehículos por fabricante
st.subheader('Histograma de los tipos de vehículos por fabricante')
fig = px.histogram(df, x='manufacturer', color='type', title='Tipos de vehículos por fabricante')
st.plotly_chart(fig)

# Histograma de la distribución de precios entre fabricantes
st.subheader('Histograma de la distribución de precios entre fabricantes')

# Menú desplegable para seleccionar los fabricantes 1 y 2
manufacturer1 = st.selectbox('Fabricante 1', df['manufacturer'].unique(), index=1)
manufacturer2 = st.selectbox('Fabricante 2', df['manufacturer'].unique(), index=2)

# Casilla de verificación para normalizar
normalized = st.checkbox('Normalizado')

# Crear un histograma con los fabricantes seleccionados (manufacturer1 y manufacturer2)
fig = go.Figure()
fig.add_trace(go.Histogram(
    x=df[df['manufacturer'] == manufacturer1]['price'],
    name=manufacturer1,
    opacity=0.6,
    histnorm='percent' if normalized else None
))
fig.add_trace(go.Histogram(
    x=df[df['manufacturer'] == manufacturer2]['price'],
    name=manufacturer2,
    opacity=0.6,
    histnorm='percent' if normalized else None
))

fig.update_layout(
    barmode='overlay' if normalized else 'group',
    xaxis_title='Precio',
    yaxis_title='Porcentaje' if normalized else 'Cantidad',
    title='Distribución de precios por fabricante'
)
st.plotly_chart(fig)

# Matriz de dispersión
st.subheader('Matriz de dispersión')
x_axis = st.selectbox('Eje X', df.columns, index=1)
y_axis = st.selectbox('Eje Y', df.columns, index=2)
color = st.selectbox('Color', df.columns, index=3)

st.subheader(f'Matriz de dispersión de {x_axis} y {y_axis} por {color}')
fig = px.scatter_matrix(df, dimensions=[x_axis, y_axis], color=color)
st.plotly_chart(fig)
