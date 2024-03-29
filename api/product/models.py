from django.db import models

from api.category.models import Category
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=60)
    discription = models.CharField(max_length=60)
    price = models.CharField(max_length=64)
    stock = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
