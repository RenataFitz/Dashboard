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

dash_df = load_data()
st.title("🎬 Online Retail Movie Analytics Dashboard")
st.write(dash_df.head())

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
