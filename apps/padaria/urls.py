from django.urls import path
from .views import list_padaria_products

app_name = 'padaria'

urlpatterns = [
    path('', list_padaria_products, name='list_padaria_products'),
]
