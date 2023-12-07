from django.db import models
from products.models import Product  

# Create your models here.
class HortifrutiProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='hortifruti_product')
