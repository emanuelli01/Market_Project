from django.db import models
from products.models import Product  

# Create your models here.
class SuplementosProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='suplementos_product')
