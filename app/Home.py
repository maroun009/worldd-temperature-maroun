import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Global Environmental Data",
    page_icon="🌐",
)

st.header("Global Environmental Data")
st.sidebar.markdown("""
        <style>
        [data-testid='stSidebarNav'] > ul {
            min-height: 60vh;
        } 
        </style>
        """, unsafe_allow_html=True)

st.sidebar.markdown("Project Team: Chris Kowalski, Betsi Flores, Maroun Hleihel")

st.markdown(
    """
    Data pulled from the following source: https://data.giss.nasa.gov/gistemp/
    """
)

greenhouse_gas = Image.open("app/img/EarthGraphic.jpg")
st.image(greenhouse_gas)
st.markdown("")

