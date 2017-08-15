import media
import fresh_tomatoes

inception = media.Movie(
    "Inception",
    "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",  # noqa
    "https://www.youtube.com/watch?v=8hP9D6kZseM")

memento = media.Movie(
    "Memento",
    "https://s-media-cache-ak0.pinimg.com/originals/59/99/d4/5999d4fec304727c714b98f9d7a30445.jpg",  # noqa
    "https://www.youtube.com/watch?v=0vS0E9bBSL0")

interstellar = media.Movie(
    "Intersellar",
    "http://www.joblo.com/posters/images/full/interstellar-poster-2.jpg",  # noqa
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

dark_knight = media.Movie(
    "The Dark Knight",
    "https://paulmmartinblog.files.wordpress.com/2011/07/the_dark_knight_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

shawshank_redemption = media.Movie(
    "Shawshank Redemption",
    "https://originalvintagemovieposters.com/wp-content/uploads/2015/05/Shawshank-Redemption-3205.jpg",  # noqa
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

star_wars = media.Movie(
    "Star Wars Episode V: The Empire Strikes Back",
    "https://s-media-cache-ak0.pinimg.com/originals/81/76/18/8176180953311ef1d6efa99af8254dcd.jpg",  # noqa
    "https://www.youtube.com/watch?v=JNwNXF9Y6kY")


# This list 'movies' will be the argument
# for the open_movies_page function to
# launch the webiste
movies = [inception,
          memento,
          interstellar,
          dark_knight,
          shawshank_redemption,
          star_wars]
fresh_tomatoes.open_movies_page(movies)
