from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
