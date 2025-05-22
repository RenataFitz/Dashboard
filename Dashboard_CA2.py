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

st.sidebar.header("🔍 Filters")

min_year, max_year = int(dash_df['year'].min()), int(dash_df['year'].max())
min_rating, max_rating = float(dash_df['rating'].min()), float(dash_df['rating'].max())

selected_year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))
selected_rating_range = st.sidebar.slider("Select Rating Range", float(min_rating), float(max_rating), (float(min_rating), float(max_rating)))

# Filter Data
filtered_df = dash_df[
    (dash_df['year'] >= selected_year_range[0]) &
    (dash_df['year'] <= selected_year_range[1]) &
    (dash_df['rating'] >= selected_rating_range[0]) &
    (dash_df['rating'] <= selected_rating_range[1])
]

st.title("🎬 Online Retail Movie Analytics Dashboard")

# Section 1: Top 10 Genres
st.subheader("FIGURE 1 | Top Ten Genres")
genre_counts = filtered_df['primary_genre'].value_counts().head(10).reset_index()
genre_counts.columns = ['primary_genre', 'count']
fig1, ax1 = plt.subplots(figsize=(12, 5))
sns.barplot(data=genre_counts, y='primary_genre', x='count', palette='deep', ax=ax1)
ax1.set_title('FIGURE: 1 | Top Ten Genre', fontsize=16, fontweight="bold")
ax1.set_xlabel('Count', fontsize=12, fontweight="bold")
ax1.set_ylabel('Genre', fontsize=12, fontweight="bold")
for bar in ax1.patches:
    ax1.text(bar.get_width() + 1000, bar.get_y() + bar.get_height() / 2, f'{int(bar.get_width()):,}', va='center', fontsize=12)
st.pyplot(fig1)
