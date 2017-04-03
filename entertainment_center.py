# This is the file (entertainment.py) that will call another file, in this
# case that file is media.py that contains the class Movie.  There are six
# pieces of information that will be passed to the Movie class as defind by
# each instance of a movie (ie. movie = Toy Story).  Those six pieces of
# information are 1) Movie Title, 2) Storyline, 3) The movies poster image,
# 4) the Youtube URL of the movie trailer, 5) the index to the global variable
# called VALID_RATINGS that contains the rating of the movie
# (where 0 = 'G', 1 = 'PG', 2 = 'PG-13 and 3 = 'R', and 6) the ratings given
# to a movie from the Rotten Tomatoes website as defined as the Tomatometer.
#
# The fresh_tomatoes file was provided as a server side file to display the
# results of the movie instances as defined below.
#
# The input to the fresh_tomatoes file is a list of the movies as defined by
# the variable 'movies'.  The output will be a html file that will display
# each instance of the movie along with all of the information defined for
# eash instance.


import fresh_tomatoes
import media

toy_story = media.Movie(
                    "Toy Story",
                    "A story of a boy and his toys that come to life",
                    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=4KPTXpQehio",
                    0, 100
                    )

avatar = media.Movie(
                    "Avatar",
                    "A marine on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                    2, 83
                    )

nemo = media.Movie(
                    "Nemo",
                    "A fish that has an adventure crossing the ocean",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Finding_Nemo.jpg/220px-Finding_Nemo.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=vbrJnqaz5Rw",
                    0, 99
                    )

smokey_and_the_bandit = media.Movie(
                    "Smokey and The Bandit",
                    "A bootleggers run from the law across the country",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/c/cb/Smokey_And_The_Bandit_Poster.jpg/220px-Smokey_And_The_Bandit_Poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=IzMpOvKxXdM",
                    1, 81
                    )

ghost_and_darkness = media.Movie(
                    "The Ghost and the Darkness",
                    "An bridge engineer hunts down two man eating lions",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/0/01/Ghostandthedarkness.jpg/250px-Ghostandthedarkness.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=1M38HWM4CTY",
                    3, 50
                    )

mission_impossible = media.Movie(
                    "Mission Impossible",
                    "IMF agent Ethan Hunt is framed for murder of fellow \
                     IMF agents",
                    "https://upload.wikimedia.org/wikipedia/en/3/3c/Missionimpossibleblurayboxset.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=QBavzf2_ook",
                    2, 63
                    )

movies = [toy_story, avatar, nemo, smokey_and_the_bandit, ghost_and_darkness,
          mission_impossible]
fresh_tomatoes.open_movies_page(movies)
