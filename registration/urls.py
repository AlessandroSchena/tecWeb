from django.urls import path, include, re_path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("registerNormale/", UserNormaleCreateView.as_view(), name="register"),
    path("registerCreatore/", UserCreatoreCreateView.as_view(), name="registerCreatore"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout")
]