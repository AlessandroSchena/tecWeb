from django.contrib.auth.models import User
from django.db import models

class Film(models.Model):
    film_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=250)
    genres = models.CharField(max_length=200, null=True, blank=True)
    original_language = models.CharField(max_length=2, null=True, blank=True)
    overview = models.CharField(max_length=1000, null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    production_companies = models.CharField(max_length=700, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)
    runtime = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)
    tagline = models.CharField(max_length=300, null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.FloatField(null=True, blank=True)
    credits = models.CharField(max_length=7200, null=True, blank=True)
    keywords = models.CharField(max_length=1300, null=True, blank=True)
    poster_path = models.CharField(max_length=32, null=True, blank=True)
    backdrop_path = models.CharField(max_length=32, null=True, blank=True)
    recommendations = models.CharField(max_length=200, null=True, blank=True)
    poster_img = models.ImageField(upload_to="images/", null=True, blank=True)

class Guardati(models.Model):
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    voto = models.FloatField(null=True, blank=True)

class DaGuardare(models.Model):
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
