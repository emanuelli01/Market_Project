# Generated by Django 4.1 on 2023-12-07 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cartitem_order_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='order',
        ),
    ]
