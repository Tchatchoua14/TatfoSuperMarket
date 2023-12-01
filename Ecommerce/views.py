from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Category, Product, Coupon, Wishlist, Livraison, Cart
# CartItem
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.views.decorators.http import require_POST
# from .cart import Cart
from .forms import CartAddProductForm, CouponApplyForm
# from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from django.http import HttpResponse, JsonResponse

import stripe
# from accountss.models import User
from django.utils.translation import gettext_lazy as _
# import random
# import string

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

@login_required
def index(request, category_slug=None):
    # nombres = Product.objects.count()
    category = None
    categories = Category.objects.all()
    product1 = Product.objects.filter(available=True).order_by('created')[:5]
    # products = Product.objects.filter(available=True)
    product2 = Product.objects.all().order_by('created')[5:10]
    product3 = Product.objects.all().order_by('created')[10:15]
    # products = Product.objects.all[0:4](available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'product1': product1, 'product2': product2, 'product3': product3}
    #  'total_quantity': total_quantity, 'subtotal': subtotal, 'total': total, 'cart_items': cart_items}
    return render(request, 'base.html', context)


def welcome(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product1 = Product.objects.all().order_by('created')[:5]
    product2 = Product.objects.all().order_by('created')[5:10]
    product3 = Product.objects.all().order_by('created')[10:15]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'product1': product1, 'product2': product2, 'product3': product3}
    return render(request, 'welcome.html', context)

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
#     return render(request, 'Ecommerce/product/list.html', context)


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





def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'detail.html', context)


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

# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
#     return redirect('Ecommerce:cart_detail')

# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('Ecommerce:cart_detail')

# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
#     coupon_apply_form = CouponApplyForm()
#     return render(request, 'cart/cart.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})

@login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render (request, 'wishlist.html', {'wishlist': wishlist})

@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect ('/wishlist/', product_id=product_id)

@login_required
def remove_from_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.remove(product)
    return redirect ('/wishlist/')

# def checkout(request):
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     intent = stripe.PaymentIntent.create(amount=1000, currency='usd',)
#     return render(request, 'checkout.html', {'client_secret': intent.client_secret})

def choix_livraison(request):
    moyens = Livraison.objects.all()
    return render(request, 'livraison.html', {'moyens': moyens})

# def process_livraison(request):
#     if request.method == 'POST':
#         moyen_id = request.POST.get('livraison')
#         moyen_livraison = Livraison.objects.get(pk=moyen_id)
#         return redirect('choix_livraison')


# def view_cart(request):
#     cart = Cart.objects.get(user=request.user)
#     cart_items = cart.cartitem_set.all()
#     cart_items1 = CartItem.objects.filter(cart=cart)
#     total_price = (item.product.price * item.quantity for item in cart_items)
#     subtotal = sum(item.product.price * item.quantity for item in cart_items)
#     total_quantity = sum(item.quantity for item in cart_items)
#     total = 0
#     for item in cart_items1:
#         item.total = item.product.price * item.quantity
#         total = item.total
#     return render (request, 'cart/cart.html', {'cart_items': cart_items, 'subtotal': subtotal, 'total': total, 'total_quantity': total_quantity })


# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect ('/cart/')

# def remove_from_cart(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     cart = Cart.objects.get(user=request.user)
#     cart_item = CartItem.objects.get(cart=cart, product=product)
#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         cart_item.save()
#     else:
#         cart_item.delete()
#     return redirect ('/cart/')

@login_required
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(amount=1000, currency='usd',)
    return render(request, 'checkout.html', {'client_secret': stripe.api_key})

def charge(request):
    if request.method =='POST':
        customer = stripe.Customer.create(
            email=request.POST['email'],
            source=request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer=customer.id,
            amount=5000,
            currency='usd',
            description='Achat via Django'
        )
        return JsonResponse({'message': 'Paiement réussi!'})



def add_to_cart(request):
    if request.method == 'POST':
        product = Product.objects.get(pk=request.POST.get('product'))
        quantity = int(request.POST.get('quantity', 1))
        cart, created = Cart.objects.get_or_create(
            user=request.user, product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart.quantity += quantity
            cart.save()
    return redirect('Ecommerce:cart_list')


class CartListView(ListView):
    template_name = "order/cart.html"
    model = Cart
    context_object_name = 'carts'

    def get_queryset(self):
        return Cart.objects.filter(
            user=self.request.user
        )
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        carts = Cart.objects.filter(
            user=self.request.user
        )
        cart_total_price = 0
        for cart in carts:
            cart_total_price += cart.total_price

        context['cart_total_price'] = cart_total_price

        return context


def modify_cart_quantity(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart.quantity = quantity
        cart.save()
    return redirect('Ecommerce:cart_list')

def delete_cart_item(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        cart.delete()
    return redirect('Ecommerce:cart_list')