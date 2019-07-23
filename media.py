import webbrowser

#Define a class Movie e suas propriedades.

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Define método de chamada para mostrar os trailers.
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
