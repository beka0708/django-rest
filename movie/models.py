from django.db import models
from user.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=127, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    genre = models.ManyToManyField(Genre)
    url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кино"
        verbose_name_plural = "Кино"


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")
    rating = models.FloatField(null=True, validators=[
        MinValueValidator(1.0, message="Рейтинг не может быть меньше 1"),
        MaxValueValidator(10.0, message="Рейтинг не может быть больше 10")
    ])
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.movie.title

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинг"


class Author(models.Model):
    movie = models.ForeignKey(Movie, models.CASCADE, related_name="author")
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} добавил в избранное кино: {self.movie.title}"

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранное"

