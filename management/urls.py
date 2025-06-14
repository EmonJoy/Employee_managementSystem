from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('manage/',manage),
    path('add-emp/',add_emp),
    path('about/', about),
    path('delete-emp/<int:emp_id>/',delete_emp),
    path('update-emp/<int:emp_id>/',update_emp),
    path('do-update-emp/<int:emp_id>/', do_update),
]
