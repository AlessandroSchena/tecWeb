from django.db import models
from prova.models import Film
from django.contrib.auth.models import User

class FilmCreati(models.Model):
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
