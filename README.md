# 🎬 Movie Recommendation System

This is a simple content-based movie recommender system built with Python and Streamlit.

## 🚀 Features

- Content-based filtering using genres and user tags
- TF-IDF vectorization and cosine similarity
- Streamlit UI for interactive recommendations

## 🗂️ Dataset

Uses [MovieLens latest-small dataset](https://grouplens.org/datasets/movielens/latest/) (`movies.csv` & `tags.csv`).

## 🧠 How It Works

- Combines genres + tags into text features
- Vectorizes using TF-IDF
- Computes similarity with cosine similarity
- Displays top 5 similar movies to selected input

## 🖥️ Run Locally

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py

## 📄 File Structure
bash
├── app.py                 # Streamlit UI
├── movie_recommender.py   # Core logic
├── requirements.txt
├── README.md
└── ml-latest-small/
    ├── movies.csv
    └── tags.csv

##  👨‍💻 Author
Name: VATSALYA MITRA NIMMAGADDA
GitHub: @vasu-vasuki
