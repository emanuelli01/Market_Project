from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.list_cart, name='list_cart'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('excluir/<int:product_id>/', views.delete_cartitem, name='delete_cartitem'),
    path('cart/decrease_quantity/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/increase_quantity/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
]