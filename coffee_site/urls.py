from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.coffee_list, name = 'coffee_list'),
    path('form',views.form),
    path('new_page',views.new_page)
]
