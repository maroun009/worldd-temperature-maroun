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

# Introduction - Identification of relationships between variables
st.markdown("## Identification of relationships between variables")

greenhouse_gas = Image.open("app/img/Forest.jpeg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Description of data distribution, outliers, etc.
st.markdown("## Description of data distribution, outliers, etc.")

# Introduction - Data Distribution for Temperature Anomalies:
st.markdown("### Data Distribution for Temperature Anomalies:")

# Introduction - Outliers
st.markdown("### Outliers")

greenhouse_gas = Image.open("app/img/Tree.jpg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Statistical Analyses Supporting Visual Findings
st.markdown("## Statistical Analyses Supporting Visual Findings")
