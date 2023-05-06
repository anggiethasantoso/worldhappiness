import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# def save_uploaded_file(file_content, file_name):
    # """
    # Save the uploaded file to a temporary directory
    # """
    # import tempfile
    # import os
    # import uuid

    # _, file_extension = os.path.splitext(file_name)
    # file_id = str(uuid.uuid4())
    # file_path = os.path.join(tempfile.gettempdir(), f"{file_id}{file_extension}")

    # with open(file_path, "wb") as file:
    #     file.write(file_content.getbuffer())

    # return file_path


def app():
    df = pd.read_csv('data.csv')
    st.title("World Happiness Factors")
    option = ["Highest to Lowest", "Lowest to Highest"]
    region_list = list(df['region'].unique())
    year = list(df['year'].unique())
    op = st.selectbox('Select Option :', option)
    op2 = st.multiselect('Select Region :', region_list)
    all_options = st.checkbox("Select all options")
    op3= st.multiselect('Select Year :', year)
    

    if all_options:
        op2 = region_list
    dfr= df[df['region'].isin(op2)]
    df_bar= dfr[dfr['year'].isin(op3)]
    df_cor= df[[ "happiness_score", "gdp_per_capita","freedom", "generosity", "health"]]
    
    # df_bar = dfr[(dfr.year == 2015)]

    # if op3 == 2015:
    #     df_bar = dfr[(dfr.year == 2015)]
    # elif op3 == 2016:
    #     df_bar = dfr[(dfr.year == 2016)]


    
    fig1 = px.bar(df_bar, x='country', y='gdp_per_capita', color='happiness_score', labels={'country':'Country','happiness_score':'Happiness Score','gdp_per_capita':'GDP per Capita'})
    fig2 = px.bar(df_bar, x='country', y='freedom', color='happiness_score', labels={'country':'Country','happiness_score':'Happiness Score','freedom':'Freedom'})
    fig3 = px.bar(df_bar, x='country', y='generosity', color='happiness_score', labels={'country':'Country','happiness_score':'Happiness Score','generosity':'Generosity'})
    fig4 = px.bar(df_bar, x='country', y='health', color='happiness_score', labels={'country':'Country','happiness_score':'Happiness Score','Health':'Health'})
    if op == "Lowest to Highest":
        fig1.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
        fig2.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
        fig3.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
        fig4.update_layout(barmode='stack', xaxis={'categoryorder': 'total ascending'})
    else:
        fig1.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
        fig2.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
        fig3.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
        fig4.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})


    tab1, tab2, tab3, tab4 = st.tabs(["GDP Per Capita", "Freedom","Generosity","Health"])
    with tab1:
        st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
    with tab2:
        st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    with tab3:
        st.plotly_chart(fig3, theme="streamlit", use_container_width=True)
    with tab4:
        st.plotly_chart(fig4, theme="streamlit", use_container_width=True)

    fig10= plt.subplots(figsize=(24, 8))

        # sns.set(rc={'figure.facecolor':'white',
        #             'xtick.color': 'black',
        #             'ytick.color': 'black',})
    st.title("Correlation Matrix and Violin Plot")
    spearman_cormatrix= df_cor.corr(method='spearman')
    sns.set()
    fig10, ax = plt.subplots(ncols=2,figsize=(24, 8))
    sns.heatmap(spearman_cormatrix, vmin=-1, vmax=1, ax=ax[0], center=0, cmap="viridis", annot=True)
    ax[0].set_title('Correlation Matrix')
    # sns.heatmap(spearman_cormatrix, vmin=-.25, vmax=1, ax=ax[1], center=0, cmap="Accent", annot=True)
    sns.violinplot(data=df, x="year", y="happiness_score",vmin=-.25, vmax=1, ax=ax[1], center=0,annot=True)
    ax[1].set_title('Distribution Graph')
    st.pyplot(fig10)

    
    # st.pyplot(fig9)



    # st.title("Upload Vector Data")

    # row1_col1, row1_col2 = st.columns([2, 1])
    # width = 950
    # height = 600

    # with row1_col2:

    #     backend = st.selectbox(
    #         "Select a plotting backend", ["folium", "kepler.gl", "pydeck"], index=2
    #     )

    #     if backend == "folium":
    #         import leafmap.foliumap as leafmap
    #     elif backend == "kepler.gl":
    #         import leafmap.kepler as leafmap
    #     elif backend == "pydeck":
    #         import leafmap.deck as leafmap

    #     url = st.text_input(
    #         "Enter a URL to a vector dataset",
    #         "https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson",
    #     )

    #     data = st.file_uploader(
    #         "Upload a vector dataset", type=["geojson", "kml", "zip", "tab"]
    #     )

    #     container = st.container()

    #     if data or url:
    #         if data:
    #             file_path = save_uploaded_file(data, data.name)
    #             layer_name = os.path.splitext(data.name)[0]
    #         elif url:
    #             file_path = url
    #             layer_name = url.split("/")[-1].split(".")[0]

    #         with row1_col1:
    #             if file_path.lower().endswith(".kml"):
    #                 gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
    #                 gdf = gpd.read_file(file_path, driver="KML")
    #             else:
    #                 gdf = gpd.read_file(file_path)
    #             lon, lat = leafmap.gdf_centroid(gdf)
    #             if backend == "pydeck":

    #                 column_names = gdf.columns.values.tolist()
    #                 random_column = None
    #                 with container:
    #                     random_color = st.checkbox("Apply random colors", True)
    #                     if random_color:
    #                         random_column = st.selectbox(
    #                             "Select a column to apply random colors", column_names
    #                         )

    #                 m = leafmap.Map(center=(40, -100))
    #                 # m = leafmap.Map(center=(lat, lon))
    #                 m.add_gdf(gdf, random_color_column=random_column)
    #                 st.pydeck_chart(m)

    #             else:
    #                 m = leafmap.Map(center=(lat, lon), draw_export=True)
    #                 m.add_gdf(gdf, layer_name=layer_name)
    #                 if backend == "folium":
    #                     m.zoom_to_gdf(gdf)
    #                 m.to_streamlit(width=width, height=height)

    #     else:
    #         with row1_col1:
    #             m = leafmap.Map()
    #             st.pydeck_chart(m)

