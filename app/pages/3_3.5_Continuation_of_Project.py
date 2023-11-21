import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image

sns.set()

st.sidebar.markdown("""
        <style>
        [data-testid='stSidebarNav'] > ul {
            min-height: 60vh;
        } 
        </style>
        """, unsafe_allow_html=True)

st.sidebar.markdown("Project Team: Chris Kowalski, Betsi Flores, Maroun Hleihel")

st.markdown("## Continuation of the Project")

st.markdown("### Avenues for Improvement")

greenhouse_gas = Image.open("app/img/DataModelling.jpg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Integration of Machine Learning")

st.markdown("### Temporal Analysis with Time Series Models")

st.markdown("### Spatial Analysis and GIS Integration")

st.markdown("### Ensemble Modelling")

greenhouse_gas = Image.open("app/img/MindMap.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Robust Handling of Extreme Events")
