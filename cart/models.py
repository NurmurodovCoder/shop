from django.db import models
from product.models import Product

class Cart(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.session_id}'

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product.name}'
    
    def get_total(self):
        return self.quantity*self.product.price