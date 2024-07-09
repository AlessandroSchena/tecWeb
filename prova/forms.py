from django import forms
from django.forms import NumberInput
from .yearChoiceForm import yearChoice


class searchForm(forms.Form):
    CHOICE_LIST = [("empty","empty"),("Action", "Action"), ("Adventure", "Adventure"), ("Animation", "Animation"), ("Comedy", "Comedy"), ("Crime", "Crime"), ("Documentary", "Documentary"), ("Drama", "Drama"), ("Family", "Family"), ("Fantasy", "Fantasy"), ("History", "History"), ("Horror", "Horror"), ("Music", "Music"), ("Mystery", "Mystery"), ("Romance", "Romance"), ("Science Fiction", "Science Fiction"), ("TV Movie", "TV Movie"), ("Thriller", "Thriller"), ("War", "War"), ("Western", "Western")]
    searchString = forms.CharField(label="Search String", max_length=100, required=False)
    genreChoice = forms.ChoiceField(choices=CHOICE_LIST, label="Genere", required=False, initial="empty")
    yearsChoice = forms.ChoiceField(choices=yearChoice(1970, 2024), label="Anno", required=False, initial="empty")
class voteForm(forms.Form):
    vote = forms.IntegerField(widget=NumberInput(attrs={'type':'range', 'step': '1', 'min':'0', 'max':'10', 'value':'10', 'oninput':"rangeValue.innerText = this.value"}))