import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

data_load_state = st.text('Loading data...')
data_load_state.text("Done! (using st.cache_data)")

# Sidebar Filters
selected_genre = st.sidebar.selectbox("Select Genre", sorted(full_df['primary_genre'].unique()))
filtered_df = full_df[full_df['primary_genre'] == selected_genre]

# Rating distribution
st.subheader(f"Rating Distribution for {selected_genre}")
rating_counts = filtered_df['rating'].value_counts().sort_index()
st.bar_chart(rating_counts)

# Release trend
st.subheader(f"Yearly Release Trend for {selected_genre}")
year_counts = filtered_df['year'].value_counts().sort_index()
st.line_chart(year_counts)

# Popular tags
st.subheader(f"Most Common Tags for {selected_genre}")
common_tags = filtered_df['tag'].value_counts().head(10)
st.write(common_tags)

# Movie preview
st.subheader("Sample Movies")
st.dataframe(filtered_df[['title', 'year', 'rating', 'tag']].dropna().head(10))