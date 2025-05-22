import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    file_id = "1Ca5CBnhUL3vhmhoqHfe3CAN62VG8n3wW"
    url = f"https://drive.google.com/uc?id={file_id}"
    return pd.read_csv(url)

dash_df = load_data()

st.title("🎬 Online Retail Movie Analytics Dashboard")


