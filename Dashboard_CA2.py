import streamlit as st
import pandas as pd
import gdown
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache_data
def load_data():
    file_id = "1UuY3I30O-AHSIw_I5QNp8-_JLZxnbrIu"
    url = f"https://drive.google.com/uc?id={file_id}"
    output = "temp_data.csv"
    gdown.download(url, output, quiet=False)
    return pd.read_csv(output)

dash_df = load_data()

st.sidebar.header("🔍 Filters")


min_year, max_year = int(dash_df['year'].min()), int(dash_df['year'].max())
selected_year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

filtered_df = dash_df[
    (dash_df['year'] >= selected_year_range[0]) &
    (dash_df['year'] <= selected_year_range[1]) 
 
]


st.title("🎬 Online Retail Movie Analytics Dashboard")


st.subheader("Top Ten Genres")
genre_counts = filtered_df['primary_genre'].value_counts().head(10).reset_index()
sns.barplot(data=genre_counts, y='primary_genre', x='count', palette='deep')
st.pyplot(fig1)

st.subheader("Movie Release Distribution Over Years")
year_counts = filtered_df['year'].value_counts().sort_index()

plt.plot(year_counts.index, year_counts.values, marker='o', linestyle='-', color='teal')
plt.grid(True)
st.pyplot(fig4)
