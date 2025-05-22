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

st.subheader("FIGURE 4 | Movie Release Distribution Over Years")

# Define full year range
min_year = int(dash_df['year'].min())
max_year = int(dash_df['year'].max())
all_years = list(range(min_year, max_year + 1))

# Add slider to select a year
selected_year = st.slider("Filter Movies by Year (Highlight)", min_year, max_year, max_year)

# Compute counts for all years
year_counts_all = dash_df['year'].value_counts().sort_index()
year_counts_all = year_counts_all.reindex(all_years, fill_value=0)

# Create color highlight (teal for all, orange for selected)
colors = ['orange' if year == selected_year else 'teal' for year in year_counts_all.index]

# Plot
fig4, ax4 = plt.subplots(figsize=(12, 5))
ax4.bar(year_counts_all.index, year_counts_all.values, color=colors)
ax4.set_title("FIGURE: 4 | Movie Release Distribution Over Years", fontsize=16, fontweight="bold")
ax4.set_xlabel("Year", fontsize=12, fontweight="bold")
ax4.set_ylabel("Number of Releases", fontsize=12, fontweight="bold")
ax4.grid(True)
st.pyplot(fig4)