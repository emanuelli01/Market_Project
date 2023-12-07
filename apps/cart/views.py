from django.shortcuts import get_object_or_404, redirect, render
from .models import CartItem
from products.models import Product
from django.http import HttpResponseRedirect
from django.urls import reverse

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('products:list_products')))

def list_cart(request):
    cart_items = CartItem.objects.filter(user=request.user).order_by('id')
    cart_total = sum(item.product.preco * item.quantity for item in cart_items)

    return render(request, 'list_cart.html', {'cart_items': cart_items, 'cart_total': cart_total})

def delete_cartitem(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product__id=product_id)
    cart_item.delete()
    return redirect('cart:list_cart')

def decrease_quantity(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product__id=product_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart:list_cart')

def increase_quantity(request, product_id):
    cart_item = get_object_or_404(CartItem, user=request.user, product__id=product_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart:list_cart')
