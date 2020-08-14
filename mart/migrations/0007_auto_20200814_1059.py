# Generated by Django 3.0.7 on 2020-08-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0006_auto_20200814_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_product',
            name='product_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='seller_product',
            name='product_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='seller_product',
            name='product_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]