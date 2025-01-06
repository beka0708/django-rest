from django.contrib import admin
from .models import Movie, Rating, Genre, Author, Favorite

admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Favorite)
