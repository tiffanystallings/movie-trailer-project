import webbrowser

class Movie():
    '''
    A template that holds information on movies and allows the
    user to play the movie's trailer.
    '''

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R', 'NC-17']
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
