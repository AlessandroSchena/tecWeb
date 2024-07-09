from django.test import TestCase
from django.contrib.auth import get_user_model
from prova.models import *
from .recommendation import recommend
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse


class RecommendTests(TestCase):

    def test_correttezza_output_user_esistente(self):
        user = User.objects.create_user('sonu', 'sonu@xyz.com', 'sn@pswrd')
        Film1 = Film(title="aserticon")
        Film1.save()
        g = Guardati(user_id=user, film_id=Film1)
        g.save()
        Film2 = Film(title="aserticon2")
        Film2.save()
        g1 = Guardati(user_id=user, film_id=Film2)
        g1.save()
        user1 = User.objects.create_user('sonu1', 'sonu@xyz.com', 'sn@pswrd')
        Guardati(user_id=user1, film_id=Film1).save()

        users = User.objects.filter(is_superuser=False).exclude(id=user1.id)
        queryset = Guardati.objects.filter(user_id=user1).values_list('film_id', flat=True)
        similarity = {}
        for u in users:
            queryset1 = Guardati.objects.filter(user_id=u).values_list('film_id', flat=True)
            intersection = queryset1.intersection(queryset)
            union = queryset1.union(queryset)
            len_int = len(intersection)
            len_union = len(union)
            s = len_int / len_union
            similarity.update({f"{u.id}": s})

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
        self.assertEquals(film_list[0], Film.objects.get(title="aserticon2"))

    def test_correttezza_output_user_inesistente(self):
        user = User.objects.create_user('sonu', 'sonu@xyz.com', 'sn@pswrd')
        a = recommend(user)
        self.assertEquals(len(a), 0)


class testHomeView(TestCase):
    def test_user_no_registrato(self):
        g = Group.objects.create(name='normale')
        g1 = Group.objects.create(name='creatore')
        permission_list = Permission.objects.all()
        g.permissions.set(permission_list)
        g1.permissions.set(permission_list)

        user = User.objects.create_user('sonu', 'sonu@xyz.com', 'sn@pswrd')
        Film1 = Film(title="aserticon")
        Film1.save()
        g = Guardati(user_id=user, film_id=Film1)
        g.save()
        Film2 = Film(title="aserticon2")
        Film2.save()
        g1 = Guardati(user_id=user, film_id=Film2)
        g1.save()
        user1 = User.objects.create_user('sonu1', 'sonu@xyz.com', 'sn@pswrd')
        Guardati(user_id=user1, film_id=Film1).save()

        response = self.client.get(reverse("home0"))
        film = Film.objects.all().order_by('-popularity')[:10]
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.context['lista_pag'].object_list, film)

    def test_user_normale(self):
        g = Group.objects.create(name='normale')
        g1 = Group.objects.create(name='creatore')
        permission_list = Permission.objects.all()
        g.permissions.set(permission_list)
        g1.permissions.set(permission_list)

        g = Group.objects.get(name='normale')
        user = User.objects.create_user('sonu', 'sonu@xyz.com', 'sn@pswrd')
        Film1 = Film(title="aserticon")
        Film1.save()
        g = Guardati(user_id=user, film_id=Film1)
        g.save()
        Film2 = Film(title="aserticon2")
        Film2.save()
        g1 = Guardati(user_id=user, film_id=Film2)
        g1.save()
        user1 = User.objects.create_user('sonu1', 'sonu@xyz.com', 'sn@pswrd')
        Guardati(user_id=user1, film_id=Film1).save()
        user.groups.add(Group.objects.get(name='normale'))
        user1.groups.add(Group.objects.get(name='normale'))

        self.client.login(username="sonu", password="sn@pswrd")
        response = self.client.get(reverse("home0"))
        film = Film.objects.all().order_by('-popularity')[:10]
        u = User.objects.get(username="sonu")
        r = recommend(u)
        self.assertEquals(response.status_code,200)
        self.assertQuerysetEqual(response.context['lista_pag'], film)
        self.assertQuerysetEqual(response.context["recommend"], r)

    def test_user_creatore(self):
        g = Group.objects.create(name='normale')
        g1 = Group.objects.create(name='creatore')
        permission_list = Permission.objects.all()
        g.permissions.set(permission_list)
        g1.permissions.set(permission_list)

        user = User.objects.create_user('sonu', 'sonu@xyz.com', 'sn@pswrd')
        user.groups.add(Group.objects.get(name='creatore'))

        self.client.login(username="sonu", password="sn@pswrd")
        response = self.client.get(reverse("home0"))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.context['lista_pag']), 0)
        self.assertEquals(len(response.context['recommend']), 0)
