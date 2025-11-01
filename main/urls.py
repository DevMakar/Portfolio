from django.urls import path

from .views import home, about, articles

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('articles/', articles, name='articles'),
]