from django.urls import path
from . import views


app_name = 'company'

urlpatterns = [
    path('', views.intro),
    path('intro/', views.intro, name='intro'),
    path('organization/', views.organization, name='organization'),
    path('history/', views.history, name='history'),
    path('link/', views.link, name='link'),
]
