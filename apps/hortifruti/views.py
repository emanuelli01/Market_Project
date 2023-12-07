from django.shortcuts import render, get_object_or_404
from .models import Product
from categories.models import Category

# Create your views here.

def list_hortifruti_products(request):
    hortifruti_category_name = 'Hortifruti'
    hortifruti_category = get_object_or_404(Category, name=hortifruti_category_name)
    hortifruti_products = Product.objects.filter(category=hortifruti_category)

    return render(request, 'hortifruti/hortifruti_list.html', {'products': hortifruti_products})
