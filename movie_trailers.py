import media
import fresh_tomatoes


imitation_game = media.Movie(
    "The Imitation Game",
    "Life and works of Alan Turing",
    "file:///Users/matthewyasul/Documents/Programming Documents/FS_Nanodegree/Projects/movie_trailer/posters/the_imitation_game.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM"
)


"""inception = media.Movie(
    "Inception",
    "A man who expose secrets by travelling into their dreams.",
    "https://pre00.deviantart.net/ab77/th/pre/i/2011/188/4/9/inception_poster_by_adamrabalais-d3lcwkz.jpg",
    "https://www.youtube.com/watch?v=YoHD9XEInc0"
)"""

wolf_of_ws = media.Movie(
    "The Wolf of Wall Street",
    "Based on the true story of Jordan Belfort",
    "http://1.bp.blogspot.com/-JrZ2BuYcpBc/UndddeSAhPI/AAAAAAAATtU/aU3mDsy3Izk/s0/The_Wolf_of_Wall_Street-poster-3.jpg",
    "https://www.youtube.com/watch?v=iszwuX1AK6A"
)

movies = [imitation_game, wolf_of_ws]

fresh_tomatoes.open_movies_page(movies)
