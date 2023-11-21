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

st.markdown("## Report")

st.markdown("### Main Contribution")

greenhouse_gas = Image.open("app/img/Report.jpg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Benchmarking")

greenhouse_gas = Image.open("app/img/Speed.jpg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("### Achievement of Project Goals")

st.markdown("##### Analysis at Global Level")

st.markdown("##### Geographical Area Analysis")

greenhouse_gas = Image.open("app/img/LineGraph.jpg")
st.image(greenhouse_gas)
st.markdown("")

st.markdown("##### Comparison with Previous Phases")

st.markdown("##### Overall Effectiveness of the Model")

