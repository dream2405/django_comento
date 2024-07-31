from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('lists', views.ProductList.as_view(), name='lists'),
    path('<int:product_id>/<str:menu>', views.detail, name='detail')
]
