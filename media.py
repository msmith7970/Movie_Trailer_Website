# This file media.py contains the class called Movie that contains as
# input movie title, storyline, poster image, youtube trailer, an index
# to the movie rating as defined by the list VALID_RATINGS, and the rating
# of the movie from the Rotten Tomatoes website as defined as the Tomatometer.

import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # initialize the data associated with the instance
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_rating, tomatometer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = self.VALID_RATINGS[movie_rating]
        self.meter = tomatometer
