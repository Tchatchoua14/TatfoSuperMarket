# Generated by Django 4.2.6 on 2023-11-27 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0008_cart_cartitem_cart_items_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
