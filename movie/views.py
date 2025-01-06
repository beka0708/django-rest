from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (GenreSerializer, MovieSerializer,
                          MovieDetailSerializer, RatingSerializer,
                          AuthorSerializer, FavoriteSerializer)
from .models import Genre, Movie, Rating, Author, Favorite


class GenreAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'


class RatingAPIView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class AuthorAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class FavoriteAPIView(ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)



