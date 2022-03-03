import imp
from unicodedata import name
from django import views
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('login', views.login, name="login"),
    path('', views.home, name='home'),
    path('signup', views.signup, name="signup"),
]

urlpatterns += staticfiles_urlpatterns()