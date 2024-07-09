from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *
class UserNormaleCreateView(CreateView):
    form_class = createUserNormaleForm
    template_name = "user_create.html"
    success_url = reverse_lazy("login")

class UserCreatoreCreateView(CreateView):
    form_class = createUserCreatoreForm
    template_name = "user_create.html"
    success_url = reverse_lazy("login")