from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('cart/', views.list_cart, name='list_cart'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('excluir/<int:product_id>/', views.delete_cartitem, name='delete_cartitem'),
]