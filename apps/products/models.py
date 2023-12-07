from django.db import models
from categories.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField('Nome', max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    date_fabrication = models.DateField('Data Fabricacao', auto_now=False, auto_now_add=False)
    is_active = models.BooleanField('Ativo', default=False)
    quantity = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering =['id']

    def __str__(self):
        return self.name
