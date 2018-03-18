from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('data/total_users.json', views.total_users),
]
