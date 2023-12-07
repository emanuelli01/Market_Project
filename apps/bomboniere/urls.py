from django.urls import path
from .views import list_bomboniere_products

app_name = 'bomboniere'

urlpatterns = [
    path('', list_bomboniere_products, name='list_bomboniere_products'),
]
