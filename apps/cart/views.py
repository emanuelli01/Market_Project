from django.shortcuts import get_object_or_404, redirect, render
from .models import CartItem
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    return redirect('cart:list_cart')

def list_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    return render(request, 'list_cart.html', {'cart_items': cart_items})

def delete_cartitem(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product__id=product_id)
    cart_item.delete()
    return redirect('cart:list_cart')

def increase_quantity(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product__id=product_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:list_cart')

def decrease_quantity(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product__id=product_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart:list_cart')