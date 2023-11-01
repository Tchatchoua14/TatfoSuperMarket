from django.shortcuts import render
from django.conf import settings
# from django.shortcuts import render, get_object_or_404
# from cart.forms import CartAddProductForm
# from .models import Category, Product
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
# from django.shortcuts import render
# from cart.cart import Cart
# from .models import OrderItem
# from .forms import OrderCreateForm

# import random
# import string
# import stripe
# stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def index(request):
    return render(request, 'base.html')

def welcome(request):
    return render(request, 'welcome.html')

def terms(request):
    return render(request, 'terms.html')

def error_404_view(request, exception):
    return render(request, '404.html')

# class HomeView(ListView):
#     model = Item
#     paginate_by = 10
#     template_name = "home.html"


# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     context = {'category': category, 'categories': categories, 'products': products}
#     return render(request, 'shop/product/list.html', context)


# class ProductListView(generic.ListView):
#     template_name = 'shop/product/list.html'

#     def get_queryset(self):
#         return Product.objects.filter(available=True)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category = None
#         if category_slug:
#             category = get_object_or_404(Category, slug=category_slug)
#         context['category'] = category
#         context['categories'] = Category.objects.all()





# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     context = {'product': product, 'cart_product_form': cart_product_form}
#     return render(request, 'shop/product/detail.html', context)


# class ProductDetialView(generic.DetailView):

#     template_name = 'shop/product/detail.html'
#     model = Product
#     form_class = CartAddProductForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = get_object_or_404(Product, 
#         id=id, slug=slug, available=True)
#         return context



# def order_create(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in cart:
#                 OrderItem.objects.create(order=order, product=item['product'],
#                                          price=item['price'], quantity=item['quantity'])
#             # clear the cart
#             cart.clear()
#             return render(request, 'order/created.html', {'order': order})
#     else:
#         form = OrderCreateForm()
#     return render(request, 'order/create.html', {'cart': cart, 'form': form})

# from django.shortcuts import render, redirect
# from django.utils import timezone
# from django.views.decorators.http import require_POST
# from .models import Coupon
# from .forms import CouponApplyForm


# @require_POST
# def coupon_apply(request):
#     now = timezone.now()
#     form = CouponApplyForm(request.POST)
#     if form.is_valid():
#         code = form.cleaned_data['code']
#         try:
#             coupon = Coupon.objects.get(code__iexact=code,
#                                         valid_from__lte=now,
#                                         valid_to__gte=now,
#                                         active=True)
#             request.session['coupon_id'] = coupon.id
#         except Coupon.DoesNotExist:
#             request.session['coupon_id'] = None
#     return redirect('cart:cart_detail')
