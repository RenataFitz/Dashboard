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

selected_genre = st.sidebar.selectbox("Select Genre", sorted(dash_df['primary_genre'].unique()))
st.subheader("Tag Frequency Within Selected Genre")
filtered_genre_tags = dash_df[dash_df['primary_genre'] == selected_genre]
genre_tag_counts = filtered_genre_tags['tag'].value_counts().head(10).reset_index()
genre_tag_counts.columns = ['Tag', 'Count']
fig6, ax6 = plt.subplots(figsize=(10, 5))
sns.barplot(data=genre_tag_counts, x='Count', y='Tag', palette='viridis', ax=ax6)
ax6.set_title(f'FIGURE: 6 | Top Tags in {selected_genre} Movies', fontsize=16, fontweight="bold")
ax6.set_xlabel('Count', fontsize=12, fontweight="bold")
ax6.set_ylabel('Tag', fontsize=12, fontweight="bold")
st.pyplot(fig6)
