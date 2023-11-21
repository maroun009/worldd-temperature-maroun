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

st.markdown("## Bibliography")

st.markdown("GARTHWAITE, J. (2023) AI predicts global warming will exceed 1.5 degrees in 2030s, Stanford News. Available at: https://news.stanford.edu/2023/01/30/ai-predicts-global-warming-will-exceed-1-5-degrees-2030s/#:~:text=The%20study%2C%20published%20Jan.,fall%20in%20the%20coming%20decade (Accessed: 10 November 2023).")