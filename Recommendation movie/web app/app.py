import streamlit as st
import pandas as pd

import pickle 

import requests



st.title("Movie recommendation system")


import requests






# print(response.json())


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZWJjMGQ3YTZiZDM1MWYyOWE1NmVlZWQwYjRjMWI4MSIsIm5iZiI6MTc0Mzc4NzUwNi4zODEsInN1YiI6IjY3ZjAxNWYyYjNlMDM1Mjg2Y2Q5NWEyMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.M9l9QM0AZFMz9lIib-fUoAcjz88pBiqBS5oDNVN9gvA"
    }
    response = requests.get(url ,params=movie_id, headers=headers)
    data=response.json()
    return "https://image.tmdb.org/t/p/original/" + data["poster_path"]


def recommends(movies):
    movie_index= movie[movie['title']==movies].index[0]
    distance=similarity[movie_index]
    movie_list= sorted(list(enumerate(distance)), reverse=True, key=lambda x : x[1])[1:6]

    recommend_movies=[]
    recommended_movie_poster=[]

    for i in movie_list:
        movie_id=movie.iloc[i[0]].movie_id
        #fetch poster from api 
        recommended_movie_poster.append(fetch_poster(movie_id))

        recommend_movies.append(movie.iloc[i[0]].title)
    return recommend_movies, recommended_movie_poster


movie_dict=pickle.load(open("movie_dict.pkl","rb"))
movie= pd.DataFrame(movie_dict)


similarity= pickle.load(open("similarity.pkl","rb"))

selected_movie = st.selectbox(
    "Choose your movie",
    movie["title"].values
)

if st.button("Recommend"):
    recommended_movie, poster=recommends(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(poster[0])

    with col2:
        st.text(recommended_movie[1])
        st.image(poster[1])

    with col3:
        st.text(recommended_movie[2])
        st.image(poster[2])
    
    with col4:
        st.text(recommended_movie[3])
        st.image(poster[3])

    with col5:
        st.text(recommended_movie[4])
        st.image(poster[4])