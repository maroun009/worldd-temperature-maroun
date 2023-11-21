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

st.markdown("""
### Introduction
* #### Technical Context
    * ###### Utilising Datasets
    * ###### Data Cleaning with Python
    * ###### Data Visualization Tools
    * ###### Project Objectives
    * ###### Technical Challenges
    * ###### Technical Opportunities
* #### Economic Context
    * ###### Economic Implications
* #### Scientific Context
    * ###### Climate Science and Data Analysis
    * ###### Understanding Climate Change
    * ###### Scientific Relevance
    * ###### Data-Driven Insights
    * ###### Contribution to Scientific Knowledge
* #### Our Roles
    * ###### Objectives
    * ###### Expertise Level of Group Members
### Understanding and Manipulation of Data
* #### Description of the Dataset(s) Used and Their Availability
* #### Ownership of Data
* #### Volume of the Dataset and Its Relevance to the Objectives
### Pre-Processing and Feature Engineering
* #### Data Cleaning and Processing Steps
    * ###### Data Cleaning
    * ###### Data Integration
    * ###### Feature Engineering
    * ###### Data Transformation
    * ###### Consideration of dimension reduction techniques
### Visualisations and Statistics
* #### Identification of relationships between variables
* #### Description of data distribution, outliers, etc.
    * ###### Data Distribution for Temperature Anomalies
    * ###### Outliers
* #### Statistical Analyses Supporting Visual Findings
"""
)