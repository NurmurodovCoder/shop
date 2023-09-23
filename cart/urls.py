from django.urls import path
from .views import cart, cart_add, sub_cart, remove_cart

urlpatterns = [
    path('', cart, name='cart'), # cart sahifasini yaratyapti
    path('cart_add/<int:product_id>/', cart_add, name='cart_add'), # cartga mahsulot qoshyapti
    path('sub_cart/<int:product_id>/', sub_cart, name='sub_cart'), #cart da "-" qilyapti
    path('remove_cart/<int:product_id>/', remove_cart, name='remove_cart'), # cart da mahsulotni ochiryapti
    path('add_cart/<int:product_id>/<str:add>/', sub_cart, name='sub_cart'), #cart da "+" qilyapti
]

