from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Category

# Create your views here.

def list_bomboniere_products(request):
    bomboniere_category_name = 'Bomboniere'
    bomboniere_category = get_object_or_404(Category, name=bomboniere_category_name)
    bomboniere_products = Product.objects.filter(category=bomboniere_category)

    return render(request, 'bomboniere/bomboniere_list.html', {'products': bomboniere_products})
