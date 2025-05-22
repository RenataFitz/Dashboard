import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data

def load_data():
    movies = pd.read_csv("movies.csv", encoding='ISO-8859-1')
    ratings = pd.read_csv("rating.csv", encoding='ISO-8859-1')
    tags = pd.read_csv("tags.csv", encoding='ISO-8859-1')
    merged = pd.merge(ratings, movies, on='movieId', how='left')
    full = pd.merge(merged, tags[['movieId', 'tag']], on='movieId', how='left')
    full = full.dropna(subset=['tag'])
    full['primary_genre'] = full['genres'].str.split('|').str[0]
    full = full.drop(['timestamp', 'genres'], axis=1)
    full['year'] = full['title'].str.extract(r'\((\d{4})\)').astype(int)
    return full

full = load_data()

st.title("🎬 Online Retail Movie Analytics Dashboard")

# Section 1: Top 10 Genres
st.subheader("FIGURE 1 | Top Ten Genres")
genre_counts = dash_df['primary_genre'].value_counts().head(10).reset_index()
genre_counts.columns = ['primary_genre', 'count']
fig1, ax1 = plt.subplots(figsize=(12, 5))
sns.barplot(data=genre_counts, y='primary_genre', x='count', palette='deep', ax=ax1)
ax1.set_title('FIGURE: 1 | Top Ten Genre', fontsize=16, fontweight="bold")
ax1.set_xlabel('Count', fontsize=12, fontweight="bold")
ax1.set_ylabel('Genre', fontsize=12, fontweight="bold")
for bar in ax1.patches:
    ax1.text(bar.get_width() + 10000, bar.get_y() + bar.get_height() / 2, f'{int(bar.get_width()):,}', va='center', fontsize=12)
st.pyplot(fig1)
