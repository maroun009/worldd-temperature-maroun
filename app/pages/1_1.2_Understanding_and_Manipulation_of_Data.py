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
st.markdown("## Understanding and Manipulation of Data")

st.markdown("### Description of the Dataset(s) Used and Their Availability")

greenhouse_gas = Image.open("app/img/LeafLightbulb.jpeg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Ownership of Data")

st.markdown("### Volume of the Dataset and Its Relevance to the Objectives")
