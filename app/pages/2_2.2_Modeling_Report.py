import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

sns.set()

st.sidebar.markdown("""
        <style>
        [data-testid='stSidebarNav'] > ul {
            min-height: 60vh;
        } 
        </style>
        """, unsafe_allow_html=True)

st.sidebar.markdown("Project Team: Chris Kowalski, Betsi Flores, Maroun Hleihel")


st.markdown("## Modeling Report")

components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQguh4RUfEzd9bdcqWUMemW4f804wRoGzdQbRRso-xap8vW1vBMmzdVSW8BY-UpYQ/embed?start=false&loop=false&delayms=60000", height=600)
