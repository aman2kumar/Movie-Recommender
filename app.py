# Two data: 1) Top 5000 movies  2) more than 45000 movies
# for 1) movies -> path -> movie_list.pkl
#        final  -> path -> final.pkl
#        movie_id = movies.iloc[int(final[index + 1][i])].movie_id
# for 2) movies -> path -> movies.pkl
#        final  -> path -> recommended_list.pkl
#        movie_id = movies.iloc[int(final[index + 1][i])].id
import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    # Api key = 9bcfe251326546a10fd48e12ea902381
    #           8265bd1679663a7ea12ac168da84d2e8
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    self_movie = []
    self_movie.append(movies.iloc[index].movie_id)
    self_movie.append(movie)
    # distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    movie_ids = []
    for i in range(9):
        movie_id = movies.iloc[int(final[index + 1][i])].movie_id
        movie_ids.append(movie_id)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[int(final[index + 1][i])].title)
    # for i in distances[1:6]:
    #     # fetch the movie poster
    #     movie_id = movies.iloc[i[0]].movie_id
    #     recommended_movie_posters.append(fetch_poster(movie_id))
    #     recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters, movie_ids, self_movie


st.header('Movie Recommender System')
# movies = pickle.load(open('movie_list.pkl','rb'))
movies = pd.read_pickle('movie_list.pkl')
# similarity = pickle.load(open('similarity.pkl','rb'))
final = pickle.load(open('final.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, movie_ids, self_movie = recommend(selected_movie)
    st.markdown('''
            <center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=60%; height=auto;/>
            </a>
            <h3></h3>
            <h4 style="font-family:verdana;">Top Recommendations for <span style="color:#7DFF33;"><i>{}</></h4>
            </center><h2></h2>'''.format(self_movie[0], fetch_poster(self_movie[0]), self_movie[1]),
            unsafe_allow_html=True
        )
    recommended_movie_names, recommended_movie_posters, movie_ids, self_movie = recommend(selected_movie)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('''
            <center>
            <p><b>{}</b></p>
            </center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=100%; height=auto;/>
            </a>
            <h1></h1>
            '''.format(recommended_movie_names[0], movie_ids[0], recommended_movie_posters[0]),
            unsafe_allow_html=True
        )
        st.markdown('''
            <center>
            <p><b>{}</b></p>
            </center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=100%; height=auto;/>
            </a>
            <h1></h1>
            '''.format(recommended_movie_names[3], movie_ids[3], recommended_movie_posters[3]),
            unsafe_allow_html=True
        )
        st.markdown('''
            <center>
            <p><b>{}</b></p>
            </center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=100%; height=auto;/>
            </a>
            <h1></h1>
            '''.format(recommended_movie_names[6], movie_ids[6], recommended_movie_posters[6]),
            unsafe_allow_html=True
        )
    with col2:
        st.markdown('''
            <center>
            <p><b>{}</b></p>
            </center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=100%; height=auto;/>
            </a>
            <h1></h1>
            '''.format(recommended_movie_names[1], movie_ids[1], recommended_movie_posters[1]),
            unsafe_allow_html=True
        )
        st.markdown('''
            <center>
            <p><b>{}</b></p>
            </center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=100%; height=auto;/>
            </a>
            <h1></h1>
            '''.format(recommended_movie_names[4], movie_ids[4], recommended_movie_posters[4]),
            unsafe_allow_html=True
        )
        st.markdown('''
            <center>
            <p><b>{}</b></p>
            </center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=100%; height=auto;/>
            </a>
            <h1></h1>
            '''.format(recommended_movie_names[7], movie_ids[7], recommended_movie_posters[7]),
            unsafe_allow_html=True
        )

    with col3:
        st.markdown('''
            <center>
            <p><b>{}</b></p>
            </center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=100%; height=auto;/>
            </a>
            <h1></h1>
            '''.format(recommended_movie_names[2], movie_ids[2], recommended_movie_posters[2]),
            unsafe_allow_html=True
        )
        st.markdown('''
            <center>
            <p><b>{}</b></p>
            </center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=100%; height=auto;/>
            </a>
            <h1></h1>
            '''.format(recommended_movie_names[5], movie_ids[5], recommended_movie_posters[5]),
            unsafe_allow_html=True
        )
        st.markdown('''
            <center>
            <p><b>{}</b></p>
            </center>
            <a style="text-decoration: none" href="https://www.themoviedb.org/movie/{}">
            <img src={} width=100%; height=auto;/>
            </a>
            <h1></h1>
            '''.format(recommended_movie_names[8], movie_ids[8], recommended_movie_posters[8]),
            unsafe_allow_html=True
        )


