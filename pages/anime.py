import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from st_vizzu import *
from st_pages import Page,show_pages,add_page_title
from ipyvizzu import Chart,Data, Config, Style,DisplayTarget
from streamlit.components.v1 import html
import pandas as pd
import ssl


with st.sidebar:
    st.header("IBME Dashboard")
    uploaded_file = st.file_uploader("Choose Your File")

if uploaded_file is None:
    st.info("Upload a file here",icon="ℹ️")
    st.stop()

@st.cache_data
def load_data(path:str):
    df = pd.read_excel(path,sheet_name=1)
    return df

df = load_data(uploaded_file)
st.table(df)

st.subheader("Data Preparation")
# rename the existing DataFrame (rather than creating a copy)
df.rename(columns={'academicyear': 'Academic_Year','TotalPaper':'Total_Paper', 'จำนวนอาจารย์': 'Number_Professors','paper/อาจารย์':'Paper_Professor_Ratio'}, inplace=True)
st.table(df)


st.subheader("Data Cleaning")
# Repalce NaN with zero on all columns
df = df.fillna(0)
st.table(df)

obj = create_vizzu_obj(df)
config_dict = {"channels": {"y": ["Academic_Year"],"x": ["Quartile1","Quartile1"] }}
style_dict = {"plot":{"paddingLeft": "12em"}}
# Animate with general dict based arguments
anim_obj = vizzu_animate(obj,config_dict=config_dict,style_dict=style_dict)
# Animate with argument based
anim_obj1 = beta_vizzu_animate(anim_obj,
    x=None,y=None,size=["Academic_Year","Quartile1"],
    label="Academic_Year", color="Quartile1",geometry="circle")
# Will use beta vizzu animate when Style reinitializing issue resolved
anim_obj2 = vizzu_animate(anim_obj1,
                {
                "y": "Quartile1",
                "x": ["Academic_Year","Quartile1"],
                "label": None,
                "size" : None,
                "geometry": "rectangle"
            }

        )
anim_obj3 = vizzu_animate(anim_obj2,
            config_dict={
            "x": "Academic_Year",
            "label": "Paper Publication"
            })

with st.container():
    vizzu_plot(anim_obj3,width=1000,height=1000)
    st.button("Animate ♻️",type='primary')
