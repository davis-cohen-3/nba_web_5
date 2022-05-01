from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='userIndex'),
    path('addPlayer', views.addPlayer, name='userAddPlayer'),
    path('submit_team', views.submit_team, name='userSubmit_team'),
]