from django.urls import path
from .views import index, store, place_order, product_detail, dashboard

urlpatterns = [

    path('', index, name='index'),
    path('store/', store, name='store'),
    path('store/<slug:category_slug>/', store, name='product_by_category'),
    path('place_order/', place_order, name='place_order'),
    path('product_detail/<slug:product_slug>/', product_detail, name='product_detail'),
    path('dashboard/', dashboard, name='dashboard'),

]
