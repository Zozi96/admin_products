# Generated by Django 3.1.3 on 2020-11-11 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_place', '0002_remove_shopplace_city'),
        ('product_registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productregistration',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_place.shopplace', verbose_name='Lugar de compra'),
        ),
    ]
