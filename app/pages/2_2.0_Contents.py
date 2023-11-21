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
### Classification of the Problem
* #### Machine Learning Type
* #### Predicting Temperature Changes
* #### Data Preprocessing
* #### Choice of Primary Performance Metric
* #### Additional Performance Metrics for Comprehensive Model Evaluation
### Model Choice and Optimization
* #### Exploring Regression Models
    * ###### Linear Regression
    * ###### Decision Tree Regressor
    * ###### Random Forest Regressor
    * ###### Model Selection
    * ###### Model Evaluation
* #### Hyperparameter Optimization
    * ###### Linear Regression
    * ###### Random Forest
* #### Model Improvement
* #### Predicting Temperature Changes for Future Years
* #### Combining Known and Future Data
* #### Future Predictions
* #### Feature Selection
* #### Future Data and Predictions
* #### Time Series Forecasting
### Interpretation of Results
* #### Analysis of Regression Model Errors
* #### Challenges in Predicting Climate-Related Variables
* #### Algorithm Selection
* #### Hyperparameter Tuning for Linear Regression
    * ###### Hyperparameter Tuning for Random Forest Regression
* #### Exploring Time Series Analysis and Forecasting Techniques
"""
)