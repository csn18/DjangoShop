# Generated by Django 4.0.1 on 2022-01-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_remove_product_size_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='Shop.ProductSize'),
        ),
    ]