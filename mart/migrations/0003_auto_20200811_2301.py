# Generated by Django 3.0.7 on 2020-08-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0002_seller_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_product',
            name='product_image',
            field=models.ImageField(upload_to=''),
        ),
    ]