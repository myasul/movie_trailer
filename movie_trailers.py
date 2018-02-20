import media
import fresh_tomatoes
import json


def retrieve_movies(filename):

    # path that contains the poster images
    poster_path = "posters/{poster_name}"

    #loads the data from the json file and transfer it to a dictionary variable
    with open(filename, 'r') as f:
        movies = json.loads(f.read())

    movie_list = []

    for movie in movies:
        #update value of poster to include absolute path
        movie["poster"] = poster_path.format(poster_name=movie["poster"])
        #creates a movie instance
        new_movie_entry = media.Movie(
            movie["title"],
            movie["storyline"],
            movie["poster"],
            movie["trailer"])
        movie_list.append(new_movie_entry)

    return movie_list

#passes a list of movie instances to display in an html page
fresh_tomatoes.open_movies_page(retrieve_movies('movie.json'))
