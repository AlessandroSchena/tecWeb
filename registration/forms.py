from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

class createUserNormaleForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit)
        g = Group.objects.get(name='normale')
        user.groups.add(g)
        return user

class createUserCreatoreForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit)
        g = Group.objects.get(name='creatore')
        user.groups.add(g)
        return user
