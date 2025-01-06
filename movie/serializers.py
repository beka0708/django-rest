from rest_framework import serializers
from .models import Genre, Movie, Rating, Author, Favorite


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "image", "authors", "average_rating"]

    def get_authors(self, obj):
        authors = obj.author.all()
        return AuthorSerializer(authors, many=True).data

    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 2)
        return None


class MovieDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Rating
        fields = ["id", "movie", "rating", "review"]


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"


