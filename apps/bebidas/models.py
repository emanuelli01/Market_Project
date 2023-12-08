from django.db import models
from products.models import Product  

# Create your models here.
class BebidasProduct(models.Model):
    product_reference = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='bebidas_product')
    product_id = models.IntegerField()
