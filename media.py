import webbrowser


class Movie():
    '''
    A template that holds information on movies and allows the
    user to play the movie's trailer.
    '''
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        '''
        Takes inputs of the movie's title (string), 
	storyline (string), poster image url (string), and 
	youtube trailer url (string) and outputs an instance 
	of Movie that holds these values.
	'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''
        Takes no inputs and produces no outputs. On running
	instance.show_trailer(), the program will open a window
	in the user's preferred browser that plays the youtube
	trailer stored in the object by __init__.
	'''
        webbrowser.open(self.trailer_youtube_url)
