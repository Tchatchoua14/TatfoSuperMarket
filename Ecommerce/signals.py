from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart, Order, Product

# @receiver(post_save, sender=Cart)
# def update_stock(sender, instance, created, **kwargs):
#     if created:
#         cart = instance.Cart
#         product = instance.Product
#         quantite_achete = cart.quantity
#         stock_actuel = product.stock
#         stock_actuel -= quantite_achete
#         product.stock = stock_actuel
#         product.save()

