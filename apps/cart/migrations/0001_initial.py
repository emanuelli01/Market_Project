# Generated by Django 4.1 on 2023-12-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carrinhos',
                'ordering': ['-added_at', 'id'],
            },
        ),
    ]
