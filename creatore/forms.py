from django import forms
from prova.models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        CHOICE_LIST = [("empty", "empty"), ("Action", "Action"), ("Adventure", "Adventure"), ("Animation", "Animation"),
                       ("Comedy", "Comedy"), ("Crime", "Crime"), ("Documentary", "Documentary"), ("Drama", "Drama"),
                       ("Family", "Family"), ("Fantasy", "Fantasy"), ("History", "History"), ("Horror", "Horror"),
                       ("Music", "Music"), ("Mystery", "Mystery"), ("Romance", "Romance"),
                       ("Science Fiction", "Science Fiction"), ("TV Movie", "TV Movie"), ("Thriller", "Thriller"),
                       ("War", "War"), ("Western", "Western")]
        model = Film
        fields = ['title', 'release_date', 'genres', 'overview', 'production_companies', 'budget', 'runtime', 'popularity', 'poster_img']
        widgets = {
            "genres": forms.Select(choices=CHOICE_LIST)
        }