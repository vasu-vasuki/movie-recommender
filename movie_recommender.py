# movie_recommender.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Path to the dataset folder
DATA_PATH = "ml-latest-small"

try:
    # Load data
    print("📁 Loading CSV files...")
    movies = pd.read_csv(os.path.join(DATA_PATH, "movies.csv"))
    tags = pd.read_csv(os.path.join(DATA_PATH, "tags.csv"))

    print("✅ CSVs loaded!")
    print("🎬 First 5 movies:\n", movies.head())

    # Preprocess tags
    tags['tag'] = tags['tag'].astype(str)
    movie_tags = tags.groupby('movieId')['tag'].apply(lambda x: ' '.join(x)).reset_index()

    # Merge with movie data
    movies = pd.merge(movies, movie_tags, on='movieId', how='left')
    movies['combined'] = movies['genres'].str.replace('|', ' ') + ' ' + movies['tag'].fillna('')

    # TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['combined'])

    # Similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(movies.index, index=movies['title'])

except Exception as e:
    print("❌ Error loading data or preprocessing:", e)

# Recommendation function
def recommend(movie_title, num_recommendations=5):
    print(f"\n🔍 Recommending movies similar to: {movie_title}")
    if movie_title not in indices:
        print("❌ Movie not found in dataset.")
        return ["Movie not found in dataset."]
    
    idx = indices[movie_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    recommended = movies['title'].iloc[movie_indices].tolist()
    print("✅ Top Recommendations:", recommended)
    return recommended

# For dropdown list
def get_movie_list():
    return sorted(movies['title'].dropna().unique())

# Manual test (run this file directly)
if __name__ == "__main__":
    test_movie = "Toy Story (1995)"
    recommend(test_movie)
