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

dash_df = load_data()

dash_df_load_state = st.text('Loading data...')
dash_df_state.text("Done! (using st.cache_data)")


st.title("🎬 Online Retail Movie Analytics Dashboard")
st.write(dash_df.head())

