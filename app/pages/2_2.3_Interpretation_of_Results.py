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

st.markdown("## Interpretation of Results")

st.markdown("### Analysis of Regression Model Errors")

st.markdown("### Residual Analysis")


st.markdown("### Outlier Detection")

st.markdown("### Model Refinements")

st.markdown("### Challenges in Predicting Climate-Related Variables")

st.markdown("### Algorithm Selection")

st.markdown("### Hyperparameter Tuning for Linear Regression")

st.markdown("### Hyperparameter Tuning for Random Forest Regression")

st.markdown("### Exploring Time Series Analysis and Forecasting Techniques")

greenhouse_gas = Image.open("app/img/ExploringTime.png")
st.image(greenhouse_gas)
st.markdown("")

greenhouse_gas = Image.open("app/img/ExploringTime1.png")
st.image(greenhouse_gas)
st.markdown("")