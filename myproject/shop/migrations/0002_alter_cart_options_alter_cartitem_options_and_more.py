# Generated by Django 5.0.6 on 2024-05-30 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Cart', 'verbose_name_plural': 'Cart'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'CartItem', 'verbose_name_plural': 'CartItem'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Products', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelTable(
            name='cart',
            table='Cart',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='CartItem',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Products',
        ),
    ]
