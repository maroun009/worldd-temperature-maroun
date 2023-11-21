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

st.markdown("## Difficulties Encountered During the Project")

st.markdown("### Main Scientific Obstacle")

st.markdown("##### Data Quality and Availability")

st.markdown("##### Model Selection and Tuning")

st.markdown("##### Inherent Uncertainty")

st.markdown("##### Changing Climate Dynamics")

greenhouse_gas = Image.open("app/img/Math.jpg")
st.image(greenhouse_gas)
st.markdown("")


st.markdown("### Forecasting")

st.markdown("##### Data Preprocessing and Cleaning")

st.markdown("##### Model Selection and Tuning")

st.markdown("##### Incorporating External Factors")

greenhouse_gas = Image.open("app/img/Forecasting.jpg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Datasets")

st.markdown("##### Data Quality and Cleaning")

st.markdown("##### Data Aggregation and Temporal Consistency")

greenhouse_gas = Image.open("app/img/DataTables.jpg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Technical/Theoretical Skills")

st.markdown("##### Advanced Time Series Modelling Techniques")

st.markdown("##### Prophet Model Implementation")

st.markdown("##### Integration of Machine Learning Models")

st.markdown("##### Statistical Analysis and Testing")

greenhouse_gas = Image.open("app/img/DataVisualization.jpg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Relevance")

st.markdown("##### Choice of Time Series Models (SARIMA and Prophet)")

st.markdown("##### Integration of Machine Learning Models")

st.markdown("##### Relevance of Prophet for Long-Term Forecasting")

st.markdown("##### Consideration of COVID-19 Impact")