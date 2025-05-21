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


