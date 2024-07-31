from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products_list'
    paginate_by = 30
    ordering = ['-pub_date', '-price']


def detail(request, product_id, menu):
    product_list = get_object_or_404(Product, pk=product_id)
    context = {'product_list': product_list, 'menu': menu}
    return render(request, 'product_detail.html', context)
