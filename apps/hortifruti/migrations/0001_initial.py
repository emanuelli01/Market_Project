# Generated by Django 4.1 on 2023-12-07 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_remove_product_quantidade_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='HortifrutiProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hortifruti_product', to='products.product')),
            ],
        ),
    ]
