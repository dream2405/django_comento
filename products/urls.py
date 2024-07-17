from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('lists', views.lists, name='lists'),
]
