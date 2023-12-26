from django import template
from django.conf import settings
from .models import Cart
# from django.contrib.auth.models import User


def totalitem(request):
    totalitem = 0
    carts = Cart.objects.filter(user=request.user.id)
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user.id))
    return {'totalitem': totalitem}
