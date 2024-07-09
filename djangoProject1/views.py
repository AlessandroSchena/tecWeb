from django.shortcuts import render
from datetime import datetime
from django.core.paginator import Paginator
from prova.models import Film, Guardati, DaGuardare
from djangoProject1 import recommendation
# Create your views here.
def home_page(request, page=1):
    film = Film.objects.all().order_by('-popularity')[:20]
    if request.user.is_authenticated:
        user = request.user
        guardati = Guardati.objects.filter(user_id=user).values_list("film_id", flat=True)
        daGuardare = DaGuardare.objects.filter(user_id=user).values_list("film_id", flat=True)
        recommend = recommendation.recommend(user)
        print(daGuardare)
    else:
        guardati = Guardati.objects.none()
        daGuardare = DaGuardare.objects.none()
        recommend = DaGuardare.objects.none()
    p = Paginator(film, 10)
    pages = p.page_range
    actual_page = p.page(page)
    page_obj = p.get_page(page)
    return render(request, template_name="home.html", context={"title": "homepage",
                                                               "guardati": guardati,
                                                               "daGuardare": daGuardare,
                                                               "recommend": recommend,
                                                               "lista_pag": page_obj,
                                                               "num_pag": pages,
                                                               "has_next": actual_page.has_next(),
                                                               "has_prev": actual_page.has_previous(),
                                                               "page": page})

