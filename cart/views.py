from django.shortcuts import redirect, render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from cart.models import Cart, CartItem, Product
from django.contrib import messages

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def cart(request):
    try:
        cart = Cart.objects.get(session_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        total = 0
        for i in cart_items:
            total += i.quantity*i.product.price
    except ObjectDoesNotExist:
        cart_items = 0
        total = 0
    context = {
        'cart_items':cart_items,
        'total':total
    }
    return render(request, 'cart.html', context)

def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(session_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(session_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
        messages.success(request, "Mahsulot savatga qoshildi !")

        cart_item.save()
    return redirect('cart')

def sub_cart(request, product_id, add=None):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(session_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if add:
        cart_item.quantity +=1
        cart_item.save()

    elif cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()

    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(session_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product, cart=cart)

    if cart_item.quantity:
        cart_item.delete()
        messages.success(request, "Mahsulot savatdan o`chirib yuborildi !")


    return redirect('cart')