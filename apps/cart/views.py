# views.py em cart
from django.shortcuts import get_object_or_404, redirect, render
from .models import CartItem
from products.models import Product

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    return redirect('cart:list_cart')
    # Lógica para adicionar o produto ao carrinho
    #cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    
    # Você pode adicionar lógica adicional aqui, por exemplo, aumentar a quantidade, etc.


def list_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)  # Substitua 'user' conforme necessário

    return render(request, 'list_cart.html', {'cart_items': cart_items})

def delete_item(request, id_product):
    product = Product.objects.get(id=id_product)
    product.delete()
    return redirect('products:list_products')

##########################