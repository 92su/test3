# pip install openpyxl
import pandas as pd
import streamlit as st
import zipfile
import base64
import os
import datetime as dt
import plotly.express as px  # pip install plotly-express
from dateutil.relativedelta import relativedelta # to add days or years
from datetime import datetime, date ,time
from PIL import Image
import matplotlib.pyplot as plt



st.sidebar.subheader('Upload Excel File')
uploaded_file = st.sidebar.file_uploader("Choose a XLSX file", type="xlsx")
if uploaded_file:
    df = pd.read_excel(uploaded_file,sheet_name=1)
    st.dataframe(df)



    st.subheader("Data Preparation")
    df.rename(columns={'academicyear': 'Academic_Year','TotalPaper':'Total_Paper', 'จำนวนอาจารย์': 'Number_Professors','paper/อาจารย์':'Paper_Professor_Ratio'}, inplace=True)
    st.table(df)


    st.subheader("Data Cleaning")
    # Repalce NaN with zero on all columns
    df = df.fillna(0)
    st.table(df)

    st.header('Number of Publication')
    st.bar_chart(df, x="Academic_Year", y=["Quartile1","Quartile2","Quartile3","Quartile4"])

    # sidebar - year selection
    st.sidebar.subheader('Pie Chart Filter Data ')
    sorted_year = sorted(df.Academic_Year.unique())
    selected_year = st.sidebar.multiselect('Academic Year',sorted_year,sorted_year)

    sorted_paper = sorted(df.Total_Paper.unique())
    selected_paper = st.sidebar.multiselect('Total Paper',sorted_paper,sorted_paper)

    df_selected_year = df[(df.Academic_Year.isin(selected_year)) & (df.Total_Paper.isin(selected_paper))]

    st.header('Display Year')
    st.write('Data:'+str(df_selected_year.shape[0])+'rows and'+ str(df_selected_year.shape[1])+ ' columns.')
    st.dataframe(df_selected_year)

        #chart_data = pd.DataFrame(columns=['Academic Year','TotalPaper'])
        #st.bar_chart(chart_data)

    df_grouped = (df.groupby(by=["Academic_Year"]).count()[["Quartile1"]].sort_values(by="Quartile1"))


    pie_chart = px.pie(df_selected_year,title="Number of Publication",values='Total_Paper',names='Academic_Year')

    st.plotly_chart(pie_chart)
