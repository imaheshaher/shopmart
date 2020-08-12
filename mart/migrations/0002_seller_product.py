# Generated by Django 3.0.7 on 2020-08-11 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, upload_to='')),
                ('product_name', models.CharField(blank=True, max_length=50)),
                ('product_price', models.IntegerField(blank=True)),
                ('product_brand', models.CharField(blank=True, max_length=50)),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mart.Seller')),
            ],
        ),
    ]
