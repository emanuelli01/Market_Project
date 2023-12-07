from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Category

# Create your views here.

def list_bebidas_products(request):
    bebidas_category_name = 'Bebidas'
    bebidas_category = get_object_or_404(Category, name=bebidas_category_name)
    bebidas_products = Product.objects.filter(category=bebidas_category)

    return render(request, 'bebidas/bebidas_list.html', {'products': bebidas_products})
