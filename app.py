import streamlit as st
#from multiapp import MultiApp
from st_vizzu import *
from st_pages import Page,show_pages,add_page_title
from ipyvizzu import Chart,Data, Config, Style,DisplayTarget
from streamlit.components.v1 import html
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

st.header("Welcome to our dashboard!")

show_pages(
    [
    Page("app.py","Streamlit Visualization"),
    Page("pages/data.py","Show Data"),
    Page("pages/anime.py","Animated Charts"),
    Page("pages/story.py","Story Animated Charts")
    ]
)

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


def create_chart():

    chart = Chart (
        width = "640px", height = "460px", display = DisplayTarget.MANUAL
    )

    data = Data()


    #df = pd.read_excel("/Data/Example to Su.xlsx",sheet_name=1)

    df = load_data(uploaded_file)

    data.add_df(df)

    chart.animate(data)

    chart.animate(

        Config(
                {
                    "x":"academicyear",
                    "y":"Quartile1",
                    "label":"academicyear",
                    "title":"IBME Paper Publication"
                }
        )
    )
    chart.animate(

        Config(

        {
                "x":["academicyear","Quartile1"],
                "label":["academicyear","Quartile1"],
                "color":"Quartile1"
            }
        )
    )
    chart.animate(Config({"x":"academicyear","y":["academicyear","Quartile1"]}))
    chart.animate(Style({"title": {"fontSize": 35}}))

# return generated html code

    return chart._repr_html_()


    # generate Chart's html code

CHART = create_chart()

html(CHART, width=650, height=370)


# Load Data
df = pd.read_excel("Data/Example to Su.xlsx",sheet_name=1)

obj = create_vizzu_obj(df)
#st.dataframe(df)


bar_obj = bar_chart(df,
            x="academicyear",
            y="Quartile1",
            title="1.Data Analysis for Paper Publication")

anim_obj = beta_vizzu_animate(bar_obj,
    x = "TotalPaper",
    y = ["Quartile1","Quartile2"],
    title = "2.Animate with:arg specific `beta_vizzu_animate()`",
    label="Paper Publication",
    color = "Genres",
    legend="color",
    sort="byValue",
    reverse=True,
    align="center",
    split=False,
)

_dict={"size":{"set":"Quartile1"},
    "geometry":"circle",
    "coorSystem":"polar",
    "title":"3.Animate with: generic dict-based 'vizzu_animate'",
    }

anim_obj2 = vizzu_animate(anim_obj,_dict)

with st.container():
    vizzu_plot(anim_obj2)
    st.button("Animate ♻️",type='primary')

@st.cache_data
def load_data(data_path:str):
    ''' Load the data
    Parameter
    ---------
    data_path : String
        Path to Data File
    Returns
    -------
        Pandas.DataFrame
    '''
    return pd.read_csv(data_path,sep=';')




# Load Data
file_path = '/Data/Example to Su.xlsx'
df = pd.read_excel(file_path,sheet_name=1) #sep=';'

# Create ipyvizzu Object
obj = create_vizzu_obj(df)
config_dict = {"channels": {"y": ["academicyear"],"x": ["Quartile1","Quartile1"] }}
style_dict = {"plot":{"paddingLeft": "12em"}}
# Animate with general dict based arguments
anim_obj = vizzu_animate(obj,config_dict=config_dict,style_dict=style_dict)
# Animate with argument based
anim_obj1 = beta_vizzu_animate(anim_obj,
    x=None,y=None,size=["academicyear","Quartile1"],
    label="academicyear", color="Quartile1",geometry="circle")
# Will use beta vizzu animate when Style reinitializing issue resolved
anim_obj2 = vizzu_animate(anim_obj1,
                {
                "y": "Quartile1",
                "x": ["academicyear","Quartile1"],
                "label": None,
                "size" : None,
                "geometry": "rectangle"
            }

        )
anim_obj3 = vizzu_animate(anim_obj2,
            config_dict={
            "x": "academicyear",
            "label": "Population (2020)"
            })
with st.container():
    vizzu_plot(anim_obj3,width=800,height=800)
