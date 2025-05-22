import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?id=1UuY3I30O-AHSIw_I5QNp8-_JLZxnbrIu"
    return pd.read_csv(url)

df = load_data()


