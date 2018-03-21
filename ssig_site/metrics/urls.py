from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='metrics-dashboard'),
    path('data/total_users.json', views.total_users),
    path('data/new_users/<str:period>.json', views.new_users),
]
