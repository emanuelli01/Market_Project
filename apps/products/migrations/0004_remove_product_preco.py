# Generated by Django 4.1 on 2023-12-04 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_preco'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='preco',
        ),
    ]
