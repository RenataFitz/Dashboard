import streamlit as st
import pandas as pd
import numpy as np
import re

st.title("🎬 Online Retail Movie Insights Dashboard")

@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv", encoding='ISO-8859-1')
    ratings = pd.read_csv("rating.csv", encoding='ISO-8859-1')
    tags = pd.read_csv("tags.csv", encoding='ISO-8859-1')
    merged = pd.merge(ratings, movies, on='movieId', how='left')
    full = pd.merge(merged, tags[['movieId', 'tag']], on='movieId', how='left')
    full['year'] = full['title'].apply(lambda x: int(re.findall(r'\((\d{4})\)', x)[0]) if re.search(r'\((\d{4})\)', x) else None)
    full['primary_genre'] = full['genres'].apply(lambda x: x.split('|')[0] if pd.notnull(x) else 'Unknown')
    full['datetime'] = pd.to_datetime(full['timestamp'], unit='s')
    return full

full_df = load_data()


full_df_load_state = st.text('Loading data...')
full_df_load_state.text("Done! (using st.cache_data)")