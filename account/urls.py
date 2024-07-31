from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('mypage/', views.my_page, name='mypage'),
    path('signup/', views.signup, name='signup'),
]
