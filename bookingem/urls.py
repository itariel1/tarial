from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('<int:id>/', views.BookDetailView.as_view(), name='book-detail'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),

]