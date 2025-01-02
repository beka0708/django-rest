from django.db import models


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
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField(null=True)
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




