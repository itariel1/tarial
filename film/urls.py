from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'film'
urlpatterns = [
    # path('anime/', views.AnimeView.as_view(), name='naruto'),
    path('movie/', views.MovieView.as_view(), name='movie'),
    # path('parser/', views.ParserAnimeView.as_view(), name='parser'),
    path('parser/', views.ParserMovieView.as_view(), name='parser'),
]