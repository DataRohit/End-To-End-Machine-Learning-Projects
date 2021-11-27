import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import requests
load_dotenv()

# getting environment variable
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

# https://api.themoviedb.org/3/movie/550?api_key=bf756d57840811ac886ba63cf5fe4601
movie_data_base_url = "https://api.themoviedb.org/3/movie/"
movie_poster_base_url = "https://image.tmdb.org/t/p/original"

# Recommender Function
def recommend(movie):
    movie_index = 0  
    # Try to find a perfect match 
    for index, title in enumerate(movies_df.title):
        if movie == title:
            movie_index = index
            break
     
    similar_movies = sorted(
        list(enumerate(similarity_matrix.loc[movie_index])), reverse=True, key=lambda x: x[1]
    )[: 6]
    
    recommended_movies_title = []
    recommended_movies_id = []
    for i in similar_movies:
        recommended_movies_title.append(movies_df.iloc[i[0]].title)  
        recommended_movies_id.append(movies_df.iloc[i[0]].id)  
    return [recommended_movies_title, recommended_movies_id]

# Getting our data from the binary files
movies_df = pd.read_pickle("./movies.pkl")
similarity_matrix = pd.read_pickle("./similarity_matrix.pkl")

# Streamlit web app code
st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a Movie To Search and Recommend", movies_df.title
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    
    image_paths = []
    for id in recommendations[1]:
        movie_data = requests.get(movie_data_base_url + str(id) + f"?api_key={TMDB_API_KEY}").json()
        image_path = movie_poster_base_url + movie_data["poster_path"]
        image_paths.append(image_path)
        
    
    col0, col1, col2 = st.columns(3)

    with col0:
        st.text(recommendations[0][0])
        st.image(image_paths[0])

    with col1:
        st.text(recommendations[0][1])
        st.image(image_paths[1])

    with col2:
        st.text(recommendations[0][2])
        st.image(image_paths[2])
        
    col3, col4, col5 = st.columns(3)
        
    with col3:
        st.text(recommendations[0][3])
        st.image(image_paths[3])

    with col4:
        st.text(recommendations[0][4])
        st.image(image_paths[4])

    with col5:
        st.text(recommendations[0][5])
        st.image(image_paths[5])