from django.urls import path
from .views import list_bebidas_products

app_name = 'bebidas'

urlpatterns = [
    path('', list_bebidas_products, name='list_bebidas_products'),
]
