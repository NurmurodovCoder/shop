from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('product_by_category', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug =models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    
    price = models.IntegerField()
    e_price = models.IntegerField(blank=True, null=True)

    image = models.ImageField(upload_to='product/')
    stock = models.IntegerField(default=100)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

