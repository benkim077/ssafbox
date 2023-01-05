from django.conf import settings
from django.db import models
from movies.models import Movie


class Theater(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)


class Screen(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    seats = models.IntegerField()


class ScreenSchedule(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField()


class ScreenSeat(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    schedule = models.ForeignKey(
        ScreenSchedule,
        on_delete=models.CASCADE,
    )
    is_reserved = models.BooleanField(default=False)
    seat_no = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
