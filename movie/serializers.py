from rest_framework import serializers
from .models import Genre, Movie, Rating, Author


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

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "image", "authors"]

    def get_authors(self, obj):
        authors = obj.author.all()
        print(authors)
        return AuthorSerializer(authors, many=True).data


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



