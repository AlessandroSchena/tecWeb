from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path("create_film/", CreateFilm, name="create_film"),
    path("add_film/", CreateFilm, name="add_film"),
    path("show_created_film/<int:page>", ShowCreatedFilm, name="ShowCreatedFilm"),
    path("modify_film/<int:id>", ModifyFilm, name="modify_film"),
    path("mod_film/", ModifyFilm, name="mod_film"),
    path("delete_film/<int:id>", DeleteFilm, name="delete_film")
]