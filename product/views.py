from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.views import _cart_id, CartItem

def index(request):
    products = Product.objects.filter(is_available=True)
    context =  {
        'products':products
    }
    return render(request, 'index.html', context)

def store(request, category_slug=None):

    if category_slug == None:
        products = Product.objects.filter(is_available=True)
    else:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=categories)
    categorys = Category.objects.all()

    if 'max_price' and 'min_price' in request.GET:
        max = request.GET.get('max_price')
        min = request.GET.get('min_price')
        products = Product.objects.filter(price__gte=min, price__lte=max)
        # products = Product.objects.filter(min<= price >=max)

    context = {
        'products':products,
        'product_count':products.count(),
        'categorys':categorys
    }
    return render(request, 'store.html', context)

def place_order(request):
    return render(request, 'place-order.html')


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart_in = CartItem.objects.filter(product=product, cart__session_id=_cart_id(request)).exists()
    context = {
        'product':product,
        'cart_in':cart_in
    }
    return render(request, 'product-detail.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')