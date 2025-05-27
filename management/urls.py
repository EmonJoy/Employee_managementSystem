from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('manage/',manage),
    path('add-emp/',add_emp),
    path('about/', about),
]
