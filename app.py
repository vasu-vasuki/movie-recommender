# app.py

import streamlit as st
from movie_recommender import recommend, get_movie_list

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")
st.title("🎬 Simple Movie Recommendation System")

# Load movie list for dropdown
movie_list = get_movie_list()
selected_movie = st.selectbox("Choose a movie you like:", movie_list)

# Button to get recommendations
if st.button("Get Recommendations"):
    st.write("🔍 Finding movies similar to:", selected_movie)
    recommendations = recommend(selected_movie)

    if recommendations and recommendations[0] != "Movie not found in dataset.":
        st.subheader("🎯 Top 5 Recommended Movies:")
        for i, movie in enumerate(recommendations, 1):
            st.markdown(f"{i}. **{movie}**")
    else:
        st.error("❌ Movie not found. Try another.")
