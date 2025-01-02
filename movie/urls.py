from django.urls import path
from .views import (GenreAPIView, MovieAPIView,
                    MovieDetailAPIView, RatingAPIView,
                    AuthorAPIView)

urlpatterns = [
    path("genre/", GenreAPIView.as_view(), name="genre-list-create"),
    path("movie/", MovieAPIView.as_view(), name="movie-list-create"),
    path("movie/<int:id>/", MovieDetailAPIView.as_view(), name="movie-id"),
    path("rating/", RatingAPIView.as_view(), name="rating-list"),
    path("authors/", AuthorAPIView.as_view(), name="author-list"),
]
