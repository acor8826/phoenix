from django.urls import path
from . import views
from .models import *
app_name = 'users'
urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
]
