from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Category

# Create your views here.

def list_suplementos_products(request):
    suplementos_category_name = 'Suplementos'
    suplementos_category = get_object_or_404(Category, name=suplementos_category_name)
    suplementos_products = Product.objects.filter(category=suplementos_category)

    return render(request, 'suplementos/suplementos_list.html', {'products': suplementos_products})
