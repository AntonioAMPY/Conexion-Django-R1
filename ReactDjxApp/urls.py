from django.contrib import admin
from django.urls import path
from ReactDjxApp.views import hola


urlpatterns = [
    path('',hola, name='hola'),
]
