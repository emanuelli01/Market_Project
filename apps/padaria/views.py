from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Category

# Create your views here.

def list_padaria_products(request):
    padaria_category_name = 'Padaria'
    padaria_category = get_object_or_404(Category, name=padaria_category_name)
    padaria_products = Product.objects.filter(category=padaria_category)

    return render(request, 'padaria/padaria_list.html', {'products': padaria_products})
