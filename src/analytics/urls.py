from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='userIndex'),
    path('queried', views.query, name='userQuery'),
    path('formChoice', views.chooseForm, name='userFormChoice'),
    path('queried2',views.query2, name='userQuery2')
]