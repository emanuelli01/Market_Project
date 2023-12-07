from django.urls import path
from .views import list_suplementos_products

app_name = 'suplementos'

urlpatterns = [
    path('', list_suplementos_products, name='list_suplementos_products'),
]
