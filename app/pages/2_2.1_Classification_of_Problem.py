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

st.markdown("## Classification of the Problem")

st.markdown("### Machine Learning Type")

st.markdown("### Predicting Temperature Changes")

st.markdown("### Data Preprocessing")

greenhouse_gas = Image.open("app/img/DataSeparation.png")
st.image(greenhouse_gas)
st.markdown("")

greenhouse_gas = Image.open("app/img/MissingValues.png")
st.image(greenhouse_gas)
st.markdown("")

greenhouse_gas = Image.open("app/img/FeatureScaling.png")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Choice of Primary Performance Metric")

st.markdown("### Additional Performance Metrics for Comprehensive Model Evaluation")
