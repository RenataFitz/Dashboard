import streamlit as st
import pandas as pd
import numpy as np

st.title("🎬 Online Retail Movie Insights Dashboard")

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