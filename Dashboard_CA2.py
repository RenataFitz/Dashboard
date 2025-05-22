import streamlit as st
import pandas as pd
import gdown
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    file_id = "1UuY3I30O-AHSIw_I5QNp8-_JLZxnbrIu"
    url = f"https://drive.google.com/uc?id={file_id}"
    output = "temp_data.csv"
    
    gdown.download(url, output, quiet=False)
    return pd.read_csv(output)

# Try to load data with error handling
try:
    dash_df = load_data()
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

st.title("🎬 Online Retail Movie Analytics Dashboard")
st.write(dash_df.head())
st.write(dash_df.shape)

