from django.db.models import Q
from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> None:
    filters = Q()
    if genres_ids:
        filters &= Q(genres__id__in=genres_ids)
    if actors_ids:
        filters &= Q(actors__id__in=actors_ids)
    return Movie.objects.filter(filters).distinct()


def get_movie_by_id(movie_id: int) -> None:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> None:
    movie = Movie.objects.create(
        title=movie_title, description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
