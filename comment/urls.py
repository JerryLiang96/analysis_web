from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r'result/<str:movie_id>', views.result, name='result'),
]
