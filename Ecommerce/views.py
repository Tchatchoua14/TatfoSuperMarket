from django.shortcuts import render
# from django.conf import settings
# from django.contrib import messages
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
# from django.views.generic import ListView, DetailView, View
# from django.shortcuts import redirect
# from django.utils import timezone
# from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
# from .models import Item, OrderItem, Order, Address, Payment, Coupon, Refund, UserProfile

# import random
# import string
# import stripe
# stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def index(request):
    return render(request, 'base.html')

# class HomeView(ListView):
#     model = Item
#     paginate_by = 10
#     template_name = "home.html"