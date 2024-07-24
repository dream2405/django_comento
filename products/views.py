from django.views.generic import ListView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products_list'
    paginate_by = 30
    ordering = ['-pub_date', '-price']
