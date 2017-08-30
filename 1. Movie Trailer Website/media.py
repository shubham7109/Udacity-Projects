# coding=utf-8

"""
Module to display movie object, attributes and instances
"""


# This movie class will help creat instance
# and save data about the title, poster and
# trailer for the movie.
class Movie(object):
    """
    Class object stores movie related information
    """

    def __init__(self,
                 movie_title,
                 movie_poster,
                 movie_trailer):
        """
        Initialize instance of class Movie
        :param movie_title: string
        :param movie_poster: string
        :param movie_trailer: string
        """
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
