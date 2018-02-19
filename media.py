import webbrowser


class Movie:
    def __init__(self, movie_title, plot, movie_img, trailer_url):
        self.title = movie_title
        self.storyline = plot
        self.poster = movie_img
        self.trailer = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer)
