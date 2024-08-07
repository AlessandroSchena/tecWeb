from prova.models import *
from django.contrib.auth import get_user_model

def recommend(user):
    if get_user_model().objects.filter(id=user.id).exists():
        users = get_user_model().objects.filter(is_superuser=False).exclude(id=user.id)
        queryset = Guardati.objects.filter(user_id=user).values_list('film_id', flat=True)
        similarity = {}
        for u in users:
            queryset1 = Guardati.objects.filter(user_id=u).values_list('film_id', flat=True)
            intersection = queryset1.intersection(queryset)
            union = queryset1.union(queryset)
            len_int = len(intersection)
            len_union = len(union)
            s = len_int / len_union
            similarity.update({f"{u.id}": s})

        print(similarity)

        m = 0
        k1 = 0
        for k, v in similarity.items():
            if v > m:
                m = v
                k1 = k

        film_k1 = Guardati.objects.filter(user_id=k1).values_list('film_id', flat=True)
        intersection = film_k1.difference(queryset)
        film_list = Film.objects.none()
        for f in intersection:
            film_list |= Film.objects.filter(id=f)
        return film_list
    else:
        return []