import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import leafmap.foliumap as leafmap
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload 
import scipy.stats as stats

import streamlit as st


st.set_page_config(page_title="World Happiness", layout="wide", page_icon="🏠",initial_sidebar_state="expanded")

apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": heatmap.app, "title": "Heatmap", "icon": "map"},
    {"func": upload.app, "title": "Visualization", "icon": "bar-chart-fill"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break

