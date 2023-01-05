from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# Create your models here.
class Movie(models.Model):
    genre = models.ManyToManyField(Genre)
    title = models.CharField(max_length=100)
    description = models.TextField()
    poster = models.CharField(max_length=200,null=True)
    release_date = models.DateField()
    score = models.FloatField()
    running_time = models.IntegerField()
    tmdb_id = models.IntegerField()
    movie_lens_id = models.IntegerField()

    def __str__(self):
        return self.title
