import streamlit as st
import streamlit.components.v1 as components

st.sidebar.markdown("""
        <style>
        [data-testid='stSidebarNav'] > ul {
            min-height: 60vh;
        } 
        </style>
        """, unsafe_allow_html=True)

st.sidebar.markdown("Project Team: Chris Kowalski, Betsi Flores, Maroun Hleihel")


st.markdown("## Exploration, Data Visualization and Data Pre-processing")

components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vQwomANmymvRBHZ_L0iDVNVqd6BJFEqUeJraFJi5e7XMov2qrqQFWamJEN0rIbcLA/embed?start=false&loop=false&delayms=60000", height=600)
