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

st.title("🎬 Online Retail Movie Analytics Dashboard")

st.sidebar.header("🔍 Filters")

min_rating = float(dash_df['rating'].min())
max_rating = float(dash_df['rating'].max())
rating_range = st.sidebar.slider("Select Rating Range", min_rating, max_rating, (min_rating, max_rating))

# Filtered dataset for all figures except Figure 4
filtered_df = dash_df[
    (dash_df['rating'] >= rating_range[0]) &
    (dash_df['rating'] <= rating_range[1])
]

# --- FIGURE 1: Top 10 Genres ---
st.subheader("FIGURE 1 | Top Ten Genres (Filtered by Rating)")
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

# --- FIGURE 2: Rating Distribution ---
st.subheader("FIGURE 2 | Rating Distribution (Filtered)")
rating_counts = filtered_df['rating'].value_counts().sort_index()
rating_df = rating_counts.reset_index()
rating_df.columns = ['rating', 'count']
fig2, ax2 = plt.subplots(figsize=(12, 5))
sns.barplot(data=rating_df, x='rating', y='count', color='lightgreen', ax=ax2)
ax2.set_title('FIGURE: 2 | Rating Distribution', fontsize=16, fontweight="bold")
ax2.set_xlabel('Rating', fontsize=12, fontweight="bold")
ax2.set_ylabel('Number of Ratings', fontsize=12, fontweight="bold")
st.pyplot(fig2)

# --- FIGURE 3: Average Rating by Genre ---
st.subheader("FIGURE 3 | Average Rating by Genre (Filtered)")
genre_means = filtered_df.groupby('primary_genre')['rating'].mean().sort_values(ascending=False).reset_index()
fig3, ax3 = plt.subplots(figsize=(12, 5))
sns.barplot(data=genre_means, x='primary_genre', y='rating', palette='rocket', ax=ax3)
ax3.set_title('FIGURE: 3 | Average Rating by Genre', fontsize=16, fontweight="bold")
ax3.set_xlabel('Primary Genre', fontsize=12, fontweight="bold")
ax3.set_ylabel('Average Rating', fontsize=12, fontweight="bold")
ax3.tick_params(axis='x', rotation=45, labelsize=10)
st.pyplot(fig3)

# --- FIGURE 4: Yearly Release Distribution (Unfiltered) ---
st.subheader("FIGURE 4 | Movie Release Distribution Over Years (Unfiltered)")

min_year = int(dash_df['year'].min())
max_year = int(dash_df['year'].max())
selected_year = st.slider("Highlight a Year", min_year, max_year, max_year)

all_years = list(range(min_year, max_year + 1))
year_counts = dash_df['year'].value_counts().sort_index().reindex(all_years, fill_value=0)

colors = ['orange' if year == selected_year else 'teal' for year in year_counts.index]
fig4, ax4 = plt.subplots(figsize=(12, 5))
ax4.bar(year_counts.index, year_counts.values, color=colors)
ax4.set_title("FIGURE: 4 | Movie Release Distribution Over Years", fontsize=16, fontweight="bold")
ax4.set_xlabel("Year", fontsize=12, fontweight="bold")
ax4.set_ylabel("Number of Releases", fontsize=12, fontweight="bold")
ax4.grid(True)
st.pyplot(fig4)

# --- FIGURE 5: Top 10 Tags ---
st.subheader("FIGURE 5 | Top Tags in Movie (Filtered)")
top_tags = filtered_df['tag'].value_counts().head(10).reset_index()
top_tags.columns = ['tag', 'count']
fig5, ax5 = plt.subplots(figsize=(12, 5))
sns.barplot(data=top_tags, x='count', y='tag', palette='magma', ax=ax5)
ax5.set_title('FIGURE: 5 | Top Tags in Movie', fontsize=16, fontweight="bold")
ax5.set_xlabel('Count', fontsize=12, fontweight="bold")
ax5.set_ylabel('Tag', fontsize=12, fontweight="bold")
st.pyplot(fig5)

# --- FIGURE 6: Tag Frequency by Selected Genre ---
st.sidebar.markdown("---")
selected_genre = st.sidebar.selectbox("Select Genre for Tag Analysis", sorted(filtered_df['primary_genre'].unique()))
st.subheader(f"FIGURE 6 | Top Tags in {selected_genre} Movies (Filtered)")
filtered_genre_tags = filtered_df[filtered_df['primary_genre'] == selected_genre]
genre_tag_counts = filtered_genre_tags['tag'].value_counts().head(10).reset_index()
genre_tag_counts.columns = ['Tag', 'Count']
fig6, ax6 = plt.subplots(figsize=(10, 5))
sns.barplot(data=genre_tag_counts, x='Count', y='Tag', palette='viridis', ax=ax6)
ax6.set_title(f'FIGURE: 6 | Top Tags in {selected_genre} Movies', fontsize=16, fontweight="bold")
ax6.set_xlabel('Count', fontsize=12, fontweight="bold")
ax6.set_ylabel('Tag', fontsize=12, fontweight="bold")
st.pyplot(fig6)