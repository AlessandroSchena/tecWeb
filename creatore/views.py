from django.shortcuts import render, redirect
from prova.models import Film
from .forms import *
from .models import *
import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def CreateFilm(request):
    if request.user.groups.filter(name='creatore').exists():
        genres = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy",
                  "History", "Horror", "Music", "Mystery", "Romance", "Science Fiction", "TV Movie", "Thriller", "War",
                  "Western"]
        if request.method == "GET":
            form = FilmForm(initial={"release_date": datetime.date.today()})
            return render(request, template_name="create_film.html", context={"form": form})
        else:
            form = FilmForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                release_date = form.cleaned_data['release_date']
                genres = form.cleaned_data['genres']
                overview = form.cleaned_data['overview']
                prod_comp = form.cleaned_data['production_companies']
                budget = form.cleaned_data['budget']
                runtime = form.cleaned_data['runtime']
                poster_img = form.cleaned_data['poster_img']
                film = Film(title=title,
                            release_date=release_date,
                            genres=genres,
                            overview=overview,
                            production_companies=prod_comp,
                            budget=budget,
                            runtime=runtime,
                            poster_img=poster_img)
                film.save()
                user = request.user
                filmCreato = FilmCreati(film_id=film, user_id=user)
                filmCreato.save()
                msg = "Film creato"
            else:
                msg = "errore nella creazione del film"
    else:
        msg = "errore nella creazione del film"
    return render(request, template_name="add_film.html", context={"msg": msg})

@login_required
def ShowCreatedFilm(request, page=1):
    if request.user.groups.filter(name='creatore').exists():
        user = request.user
        film = FilmCreati.objects.filter(user_id=user)
        p = Paginator(film, 5)
        pages = p.page_range
        actual_page = p.page(page)
        page_obj = p.get_page(page)
        return render(request,
                      template_name="ShowCreatedFilm.html",
                      context={ "lista_pag": page_obj,
                                "num_pag": pages,
                                "has_next": actual_page.has_next(),
                                "has_prev": actual_page.has_previous(),
                                "page": page})

@login_required
def ModifyFilm(request, id):
    if request.user.groups.filter(name='creatore').exists():
        if request.method == "GET":
            film = FilmCreati.objects.get(id=id).film_id
            form = FilmForm(initial={"title": film.title, "release_date": film.release_date, "genres": film.genres,
                                     "overview": film.overview, "production_companies": film.production_companies,
                                     "budget": film.budget, "runtime": film.runtime, "poster_img": film.poster_img})
            return render(request, template_name="modify_film.html", context={"form": form})
        else:
            form = FilmForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                release_date = form.cleaned_data['release_date']
                genres = form.cleaned_data['genres']
                overview = form.cleaned_data['overview']
                prod_comp = form.cleaned_data['production_companies']
                budget = form.cleaned_data['budget']
                runtime = form.cleaned_data['runtime']
                poster_img = form.cleaned_data['poster_img']
                popularity = form.cleaned_data['popularity']
                film = Film(title=title, release_date=release_date, genres=genres, overview=overview,
                            production_companies=prod_comp, budget=budget, runtime=runtime, poster_img=poster_img,
                            popularity=popularity)
                film.save()
                user = request.user
                filmCreato = FilmCreati(film_id=film, user_id=user)
                filmCreato.save()
                msg = "Film modificato"
            else:
                msg = "errore nella modifica del film"
    else:
        msg = "errore nella modifica del film"
    return render(request, template_name="mod_film.html", context={"msg": msg})

@login_required
def DeleteFilm(request, id):
    if request.user.groups.filter(name='creatore').exists():
        film = FilmCreati.objects.get(id=id)
        film.film_id.delete()
        msg = "Film eliminato"
    else:
        msg = "film non eliminato non si hanno i permessi"
    return render(request, template_name="delete_film.html", context={"msg": msg})