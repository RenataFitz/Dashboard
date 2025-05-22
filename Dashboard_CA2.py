import streamlit as st
import pandas as pd

import seaborn as sns

@st.cache_data
def load_data():
    return pd.read_csv("dash_df.csv")  

# Load the data
dash_df = load_data()

# Streamlit Title
st.title("🎬 Online Retail Movie Analytics Dashboard")


