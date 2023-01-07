import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import preprocessor,helper
from matplotlib import style
from PIL import Image

import plotly
import plotly.express as px
import plotly.graph_objects as go

import cufflinks as cf
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot

pyo.init_notebook_mode(connected=True)
cf.go_offline()

df=pd.read_csv('country_wise_latest (3).csv')


df=preprocessor.processor(df)





st.sidebar.title("covid  Analysis")

image = Image.open('covid.jpg')

st.sidebar.image('covid.jpg')

user_menu=st.sidebar.radio(
    'select an option',
    ('Overall Analysis','Country wise anlysis','Confirmed_case',	'Deaths_case',	'Recovered_case')


)

if user_menu=='Overall Analysis':


    st.title("Overall Analysis")

    x=df.style.background_gradient(cmap='Reds')


    st.dataframe(x)

if user_menu=='Country wise anlysis':
    st.sidebar.header("Country Wise Analysis")

    new_df = helper.country_list(df)


    selected_country = st.sidebar.selectbox("select country", new_df)

    country = helper.country_wise(df, selected_country)

    

    st.dataframe(country)





if user_menu =='Confirmed_case':
    st.title('country with confirmed cases')
    df2 = df.groupby('country')['Confirmed'].sum().sort_values(ascending=False).reset_index()
    x=df2.style.background_gradient(cmap='Reds')
    st.dataframe(x)

    df3= df.groupby('country')['Confirmed'].sum().sort_values(ascending=False).reset_index().head()

    st.title('Top 5 confirmed country')

    fig = px.line(df3, x="country", y='Confirmed')



    st.plotly_chart(fig)

if user_menu=='Deaths_case':
    x=df.groupby('country')['Deaths'].sum().sort_values(ascending=False).reset_index()
    st.title('country with death cases')
    st.dataframe(x)
    df4 = df.groupby('country')['Deaths'].sum().sort_values(ascending=False).reset_index().head()

    st.title('Top 5 country')

    fig=px.line(df4,x='country',y='Deaths')

    st.plotly_chart(fig)

if user_menu=='Recovered_case':
    df5=df.groupby('country')['Recovered'].sum().sort_values(ascending=False).reset_index()
    st.title('Recovered country')
    x=df5.style.background_gradient(cmap='Reds')
    st.dataframe(x)
    x=df.groupby('country')['Recovered'].sum().sort_values(ascending=False).reset_index().head()
    st.title(' top5 country ')
    fig = px.line(x, x='country', y='Recovered')
    st.plotly_chart(fig)












































