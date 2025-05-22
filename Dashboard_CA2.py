import streamlit as st
import pandas as pd

@st.cache_data
def load_data():

    dash_df = "https://drive.google.com/file/d/1Ca5CBnhUL3vhmhoqHfe3CAN62VG8n3wW/view?usp=drive_link"
    return pd.read_csv(dash_df)  

# Load the data
dash_df = load_data()

# Streamlit Title
st.title("🎬 Online Retail Movie Analytics Dashboard")


