from django import template
from django.conf import settings
from .models import Cart
# from django.contrib.auth.models import User


def totalitem(request):
    totalitem = 0
    carts = Cart.objects.filter(user=request.user.id)
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user.id))
    cart_total_price = 0
    for cart in carts:
        cart_total_price += cart.total_price
    return {'totalitem': totalitem, 'carts': carts, 'cart_total_price': cart_total_price}
