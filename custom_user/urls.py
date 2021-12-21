from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('login/', views.LoginUser.as_view(), name='login'),
]