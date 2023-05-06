import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode



def app():
    
    st.title("World Happiness Index")
    st.image("image.png", use_column_width='always')

    st.write(
        """
        The World Happiness Report is a publication of the Sustainable Development Solutions Network, powered by the Gallup World Poll data. 
        The World Happiness Report reflects a worldwide demand for more attention to happiness and well-being as criteria for government policy. 
        It reviews the state of happiness in the world today and shows how the science of happiness explains personal and national variations in happiness.
        The Happiness Score is explained by the following factors:

• GDP per capita

• Healthy Life Expectancy

• Freedom to make life choices

• Generosity


    """
    )
    
    df1 = pd.read_csv('data.csv')
    option = ["Highest to Lowest", "Lowest to Highest"]
    year = list(df1['year'].unique())
    op = st.selectbox('Select Option :', option)
    op1 = st.multiselect('Select Year :', year)
    dfr= df1[df1['year'].isin(op1)]
    fig1 = px.bar(dfr, x='country', y='happiness_score', labels={'country':'Country','happiness_score':'Happiness Score'})
    if op == "Lowest to Highest":
        fig1.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
    else:
        fig1.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig1,use_container_width=True)

    df = pd.read_csv('data.csv')
    region_list = list(df['region'].unique())
    regions = st.multiselect('Select Region :', region_list)
    dfr= df[df['region'].isin(regions)]
    # st.write(dfr)
    country_list = list(dfr['country'].unique())
    countries = st.multiselect('Select Country :', country_list)
    all_options = st.checkbox("Select all options")
    if all_options:
        countries = country_list
    st.header("Country Happiness by Year : {}".format(", ".join(countries)))

    dfs = {country: df[df["country"] == country] for country in countries}

    fig = go.Figure()
    for country, df in dfs.items():
        fig = fig.add_trace(go.Scatter(x=df["year"], y=df["happiness_score"], name=country))
    st.plotly_chart(fig,use_container_width=True)
        
        
        


