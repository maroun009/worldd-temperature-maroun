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

# Introduction - Data Cleaning and Processing Steps
st.markdown("## Data Cleaning and Processing Steps")

greenhouse_gas = Image.open("app/img/EarthCartoon.jpg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Data Cleaning")

# Introduction - Data Integration
st.markdown("### Data Integration")

greenhouse_gas = Image.open("app/img/SustainableTechnology.jpeg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Feature Engineering")


# Introduction - Data Transformation:
st.markdown("### Data Transformation")


# Introduction - Consideration of dimension reduction techniques
st.markdown("### Consideration of dimension reduction techniques")

