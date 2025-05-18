import streamlit as st
import pandas as pd
import numpy as np

st.title("Movie Dashboard")

DATE_COLUMN='time_stamp'

DATA_URL = ('https://github.com/CCT-Dublin/machine-learning-for-business-ca2-RenataFitz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(264505)
data_load_state.text("Done! (using st.cache_data)")