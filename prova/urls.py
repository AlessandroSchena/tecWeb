from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("list/", lista_film, name="list"),
    path("search/", search_film, name="search"),
    path("search/<str:query>/<str:genre>/<str:year>/<int:page>/", lista_film2, name="list1"),
    path("search/<str:genre>/<str:year>/<int:page>", lista_film1, name="list2"),
    path("add_guardati/<int:id_film>/", add_guardati, name="add_guardati"),
    path("add_guardati/<int:id_film>", add_voto, name="add_voto"),
    path("lista_guardati/<int:page>", lista_guardati, name="lista_guardati"),
    path("profilo/", profilo, name="profilo"),
    path("film/<int:film_id>", film_overview, name="film_overview"),
    path("add_DaGuardare/<int:id_film>/", add_DaGuardare, name="add_DaGuardare"),
    path("lista_DaGuardare/<int:page>", lista_DaGuardare, name="lista_DaGuardare"),
    path("delete/<int:id>", delete_filmDaGuardare, name="delete_filmDaGuardare")
]