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

# Introduction - Technical Context
st.markdown("## Technical Context")

st.markdown("### Utilizing Datasets")

greenhouse_gas = Image.open("app/img/GreenHouseGasesPollution.jpg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Data Cleaning with Python
st.markdown("### Data Cleaning with Python")

# Introduction - Data Visualization Tools:
st.markdown("### Data Visualization Tools: ")

greenhouse_gas = Image.open("app/img/TreeDataGraph.jpeg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Project Objectives:
st.markdown("### Project Objectives: ")

# Introduction - Technical Challenges:
st.markdown("### Technical Challenges: ")

# Introduction - Technical Opportunities:
st.markdown("### Technical Opportunities: ")

greenhouse_gas = Image.open("app/img/CarbonFootprint.jpg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Economic Context:
st.markdown("## Economic Context:  ")

# Introduction - Economic Implications
st.markdown("### Economic Implications: ")

greenhouse_gas = Image.open("app/img/AutumLeaves.jpg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Scientific Context:
st.markdown("## Scientific Context:  ")

greenhouse_gas = Image.open("app/img/CO2.jpeg")
st.image(greenhouse_gas)
st.markdown("")

# Introduction - Our Roles:\n
st.markdown("## Our Roles")


st.markdown("### Objectives")

st.markdown("### Our team consists of members with complementary skills and expertise")
