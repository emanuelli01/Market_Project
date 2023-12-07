from django.db import models
from products.models import Product  

# Create your models here.
class BomboniereProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='bomboniere_product')
