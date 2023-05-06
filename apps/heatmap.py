import streamlit as st
import plotly.express as px
import pandas as pd
import geopandas as gpd
import json
import plotly.graph_objects as go

df = pd.read_csv('data.csv')
df_2019 = df[(df.year == 2019)]

def app():

    from urllib.request import urlopen
    st.title("Country World Happiness by Year")    

    with open('/home/em/Documents/Anggietha/Datsci/Datsci/countries.geojson') as response:
        ccaa = json.load(response)

    fig = px.choropleth_mapbox(
        data_frame = df,           
        geojson = ccaa,                     
        featureidkey = 'properties.ADMIN', 
        locations = df['country'],              
        color = df['happiness_score'],               
        animation_frame = df['year'],
        mapbox_style = 'open-street-map',
        center = dict(lat = 40.0, lon = -3.72),
        zoom = 4)
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=6.6,
        mapbox_center={"lat": 46.8, "lon": 8.2},
        width=800,
        height=600,
    )

    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    st.plotly_chart(fig, theme=None, use_container_width=True,height=3000)


