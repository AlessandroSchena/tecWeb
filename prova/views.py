from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Film, Guardati, DaGuardare
from django.core.paginator import Paginator
from .forms import searchForm, voteForm
from django.contrib.auth.decorators import login_required
from djangoProject1 import recommendation

def lista_film(request):
    film = Film.objects.all().order_by('-popularity')[:20]
    return render(request=request, context={"lista_film": film}, template_name="lista_film.html")

def search_film(request):
    if request.method == "GET":
        form = searchForm()
        return render(request, template_name="search_film.html", context={"form": form})
    else:
        form = searchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['searchString']
            genre = form.cleaned_data['genreChoice']
            year = form.cleaned_data['yearsChoice']
            print(q)
        if q == '':
            if year == 'empty':
                return redirect("list2", page=1, genre=genre, year=year)
            else:
                return redirect("list2", page=1, genre=genre, year=int(year))
        elif q=='' and genre == 'empty' and year == 'empty':
            return render(request, template_name="search_error.html")
        elif year=='empty':
            return redirect("list1", query=q, page=1, genre=genre, year=year)
        else:
            return redirect("list1", query=q, page=1, genre=genre, year=int(year))


def lista_film2(request, query, genre, year, page=1):
    if genre == 'empty' and year == 'empty':
        film_list = Film.objects.filter(title__contains=query)[:20]
    elif year == 'empty':
        film_list = Film.objects.filter(title__contains=query, genres__contains=genre)[:20]
    elif genre == 'empty':
        film_list = Film.objects.filter(title__contains=query, release_date__year=year)
    else:
        film_list = Film.objects.filter(title__contains=query, release_date__year=year, genres__contains=genre)


    p = Paginator(film_list, 5)
    pages = p.page_range
    actual_page = p.page(page)
    page_obj = p.get_page(page)
    return render(request, template_name="lista_film2.html", context={
        "title": "homepage",
        "lista_pag": page_obj,
        "num_pag": pages,
        "has_next": actual_page.has_next(),
        "has_prev": actual_page.has_previous(),
        "page": page,
        "q": query,
        "genre": genre,
        "year": year
    })

def lista_film1(request, genre, year, page=1):
    if year == 'empty':
        film_list = Film.objects.filter(genres__contains=genre)[:20]
    elif genre == 'empty':
        film_list = Film.objects.filter(release_date__year=year)[:20]
    else:
        film_list = Film.objects.filter(release_date__year=year, genres__contains=genre)[:20]


    p = Paginator(film_list, 5)
    pages = p.page_range
    actual_page = p.page(page)
    page_obj = p.get_page(page)
    return render(request, template_name="lista_film1.html", context={
        "title": "homepage",
        "lista_pag": page_obj,
        "num_pag": pages,
        "has_next": actual_page.has_next(),
        "has_prev": actual_page.has_previous(),
        "page": page,
        "genre": genre,
        "year": year
    })

@login_required
def add_guardati(request, id_film):
    if request.method == "GET":
        form = voteForm()
        id_user = request.user
        if Guardati.objects.filter(film_id=id_film, user_id=id_user).exists():
            msg = "già in lista guardati"
            g1 = Guardati.objects.get(film_id=id_film, user_id=id_user)
        else:
            film = Film.objects.get(id=id_film)
            g = Guardati(user_id=id_user, film_id=film)
            g.save()
            msg = "film inserito in lista guardati"
            dg = DaGuardare.objects.filter(user_id=id_user, film_id=film)
            g1=Guardati.objects.none()
            if dg.exists():
               dg.delete()
        return render(request, template_name="add_guardati.html", context={"msg": msg, "id_film": id_film, "guardati": g1, "form": form})
    else:
        form = voteForm(request.POST)
        if form.is_valid():
            voto = form.cleaned_data['vote']
            print(voto)
            film = Film.objects.get(id=id_film)
            g = Guardati.objects.get(film_id=film, user_id=request.user)
            g.voto = voto
            film.vote_average = ((film.vote_average * film.vote_count) + voto) / (film.vote_count + 1)
            film.vote_count += 1
            film.save()
            g.save()
            return redirect("add_voto", id_film=id_film)

@login_required
def add_voto(request, id_film):
    return render(request, template_name="add_voto.html", context={"id_film": id_film})

@login_required
def profilo(request):
    return render(request, template_name="profilo_utente.html")

@login_required
def lista_guardati(request, page=1):
    id_utente = request.user.id
    guardati = Guardati.objects.filter(user_id=id_utente)
    p = Paginator(guardati, 5)
    pages = p.page_range
    actual_page = p.page(page)
    page_obj = p.get_page(page)
    return render(request, template_name="lista_guardati.html", context={
        "title": "homepage",
        "lista_pag": page_obj,
        "num_pag": pages,
        "has_next": actual_page.has_next(),
        "has_prev": actual_page.has_previous(),
        "page": page
    })

def film_overview(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, template_name="film_overview.html", context={"film": film})

@login_required
def add_DaGuardare(request, id_film):
    id_user = request.user
    if Guardati.objects.filter(film_id=id_film, user_id=id_user).exists():
        msg = "già in lista da guardare"
        g1 = DaGuardare.objects.get(film_id=id_film, user_id=id_user)
    else:
        film = Film.objects.get(id=id_film)
        g = DaGuardare(user_id=id_user, film_id=film)
        g.save()
        g1 = DaGuardare.objects.none()
        msg = "film inserito in lista da guardare"
    return render(request, template_name="DaGuardare.html", context={"msg": msg, "id_film": id_film, "DaGuardare": g1})

@login_required
def lista_DaGuardare(request, page=1):
    id_utente = request.user.id
    daGuardare = DaGuardare.objects.filter(user_id=id_utente)
    p = Paginator(daGuardare, 5)
    pages = p.page_range
    actual_page = p.page(page)
    page_obj = p.get_page(page)
    return render(request, template_name="lista_DaGuardare.html", context={
        "title": "homepage",
        "lista_pag": page_obj,
        "num_pag": pages,
        "has_next": actual_page.has_next(),
        "has_prev": actual_page.has_previous(),
        "page": page
    })

@login_required
def delete_filmDaGuardare(request, id):
    film = DaGuardare.objects.filter(id=id)
    f = DaGuardare.objects.get(id=id).film_id
    if film.exists():
        film.delete()
        msg = f"film {f.title} eliminato"
    else:
        msg = f"film {f.title} non eliminato"
    return render(request, template_name="delete_DaGuardare.html", context={"msg": msg})
