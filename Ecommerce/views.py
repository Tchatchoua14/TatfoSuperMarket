from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Category, Product, Coupon, Wishlist, Livraison, Cart, Newsletters, Order, BillingDetails, Verification
# CartItem
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.views.decorators.http import require_POST
# from .cart import Cart
from django.core.mail import send_mail
from .forms import CartAddProductForm, CouponApplyForm
# from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm
from django.http import HttpResponse, JsonResponse
import requests 
import stripe
import uuid
# from accountss.models import User
from django.utils.translation import gettext_lazy as _
from .forms import BillingDetailsForm, NewlettersForm
# import random
# import string

stripe.api_key = settings.STRIPE_SECRET_KEY

notchpay = settings.NOTCHPAY_SECRET_KEY


# Create your views here.

@login_required
def index(request, category_slug=None):
    # nombres = Product.objects.count()
    category = None
    categories = Category.objects.all()
    product1 = Product.objects.filter(available=True).order_by('created')[:5]
    # product7 = Product.objects.filter(available=True)
    product2 = Product.objects.all().order_by('created')[5:10]
    product3 = Product.objects.all().order_by('created')[10:15]
    # products = Product.objects.all[0:4](available=True)
    totalitem = 0
    carts = Cart.objects.filter(user=request.user)
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart_total_price = 0
    for cart in carts:
        cart_total_price += cart.total_price
    context = {'category': category, 'categories': categories, 'product1': product1, 'product2': product2, 'product3': product3, 'totalitem': totalitem, 'carts': carts, 'cart_total_price': cart_total_price}
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

def newsletter(request):
    if request.method == 'POST':
        form = NewlettersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Ecommerce:home')
    else:
        form = NewlettersForm()
    return render(request, 'base.html', {'form': form})
        

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

def search(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if request.method == "GET":
        name = request.GET.get("q")
        if name is not None:
            products = Product.objects.filter(Q(name__icontains=name) | Q(price__icontains=name))
    # products = Product.objects.all[0:4](available=True)
    totalitem = 0
    carts = Cart.objects.filter(user=request.user)
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart_total_price = 0
    for cart in carts:
        cart_total_price += cart.total_price
    context = {'category': category, 'categories': categories, 'products': products, 'totalitem': totalitem, 'carts': carts}
    return render(request, 'search.html', context)


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


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('Ecommerce:checkout')

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

# @login_required
def view_wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render (request, 'wishlist.html', {'wishlist': wishlist})

# @login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    return redirect ('/wishlist/', product_id=product_id) 

# @login_required
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
    # orders = Order.objects.create(user=request.user)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(amount=1000, currency='usd',)
    totalitem = 0
    carts = Cart.objects.filter(user=request.user)
    if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user)) 
    cart_total_price = 0
    shipping_amount = 2000
    for cart in carts:
        cart_total_price += cart.total_price
        cart_total = cart_total_price + shipping_amount
    return render(request, 'checkout.html', {'client_secret': stripe.api_key, 'totalitem': totalitem, 'carts':carts, 'cart_total_price': cart_total_price, 'cart_total': cart_total, 'shipping_amount': shipping_amount })

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

def success(request):
    return render(request, "paysuccess.html")

def cancel(request):
    return render(request, "paycancel.html")


def order(request):
    cart = Cart.objects.filter(user=request.user)
    user = request.user
    try:
        billing_info = BillingDetails.objects.get(user=user)
    except BillingDetails.DoesNotExist:
        billing_info = None

    if request.method == 'POST':
        form = BillingDetailsForm(request.POST, instance=billing_info)
        if form.is_valid():
            billing_instance = form.save(commit=False)
            billing_instance.user = user
            billing_instance.save()
            return redirect('Ecommerce:home')
            for item in cart:
                Order.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request, 'order/create.html', {'order': order})
    else:
        form = BillingDetailsForm(instance=billing_info)
    return render(request, 'order/create.html', {'cart': cart, 'form': form})



from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new




# new
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
         
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                # success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                # cancel_url=domain_url + 'cancelled/',
                success_url=settings.PAYMENT_SUCCESS_URL,
                cancel_url=settings.PAYMENT_CANCEL_URL,
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'T-shirt',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '2000',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


    #  $payload = Payment::initialize([
    #             'amount' => $product->price,
    #             'email' => Auth::user()->email,
    #             'name' => Auth::user()->name,
    #             'currency' => 'XAF',
    #             'reference' => Auth::id() . '-' . uniqid(), 
    #             'callback' => route('notchpay-callback'),
    #             'description' => $product->description,
    #         ]); 

    #    try {
    #         $payload = Payment::initialize([
    #             // 'amount' => $product->price,
    #             'amount' => $subtotal,
    #             'email' => Auth::user()->email,
    #             'name' => Auth::user()->name,
    #             'currency' => 'XAF',
    #             'reference' => Auth::id() . '-' . uniqid(), 
    #             'callback' => route('notchpay-callback'),
    #             'description' => $product->description,
    #         ]);

    # // sb.Cdo6b4O77BATFtsPUCxlp3buDWtAjqQSV7hXX8fHSBkXC724BO9ncKwxKGfUIqQpsoYojcFYqJAr6GjfUgJ0XVGw1mEI2I4zg00bzfHx8K5mynoKRMXLNiwDLGTyw

@login_required
def process(request):
    # product = get_object_or_404(Product, pk=product_id)
    # description = product.description
    # price = product.price
    carts = Cart.objects.filter(user=request.user)
    email= request.user.email
    cart_total_price = 0
    for cart in carts:
        cart_total_price += cart.total_price
    amount = cart_total_price
    # amount = 5000
    currency = 'XAF'
    description = "achat via Notchpay"
    # email = "customer@email.com"
    # phone = 655728267

    api_url = 'https://api.notchpay.co/payments/initialize'
    headers = {
        'Authorization': f'{notchpay}'
    }

    data = {
        'amount' : amount,
        'currency' : currency,
        'description' : description, 
        'email' : email,
        # 'phone' : phone
    }

    response = requests.post(api_url, data=data, headers=headers)
    if response.status_code == 201:
        # authorization_url = "https://pay.notchpay.co/webcheckout/p.XpAviOtvFXpvuPPHp28Nv7W46NW00mYyryg0FBHDCSDzwGMZGre68OtIXJaVAfM6K3TAY20KyEXf9qV6Dc3FOSVQZ3jf1xTu"
        # if authorization_url:
        #     return redirect(authorization_url)
        # return JsonResponse({'message': 'paiement réussi'})
        api = response.json()
        # api = response.text
        # print(api)
    # return HttpResponse (api)
        if 'authorization_url' in api:
            authorization_url = api['authorization_url']
            # print(authorization_url)
            return redirect(authorization_url)
        return render(request, 'paysuccess.html', {'authorization_url': authorization_url})
    else:
        # return JsonResponse({'error': 'Erreur lors du paiment'})
        return render(request, 'paycancel.html')



# class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    # def post(self, request, *args, **kwargs):
    #     price = Product.objects.get(id=self.kwargs["pk"])

    #     checkout_session = stripe.checkout.Session.create(
    #         payment_method_types=["card"],
    #         line_items=[
    #             {
    #                 "price_data": {
    #                     "currency": "usd",
    #                     "unit_amount": int(product.price) * 100,
    #                     "product_data": {
    #                         "name": product.name,
    #                         "description": product.description,
    #                         "images": [
    #                             f"{settings.BACKEND_DOMAIN}/{product.image1}"
    #                         ],
    #                     },
    #                 },
    #                 "quantity": product.quantity,
    #             }
    #         ],
    #         metadata={"product_id": product.id},
    #         mode="payment",
    #         success_url=settings.PAYMENT_SUCCESS_URL,
    #         cancel_url=settings.PAYMENT_CANCEL_URL,
    #     )
    #     return redirect('Ecommerce:cart_list')


def send_email_after_registration(email, token):
    subject = "Verify Email"
    message = f"""
    Dear Sir/Madam,

    ATTN : Please do not reply to this email.This mailbox is not monitored and you will not receive a response.

    Your Verification Email is Given bellow 👇
    Click on the link to verify your account https://http://127.0.0.1:8000/account-verify/{token}

    If you have any queries, Please contact us at,

    TatfoSuperMarket,
    Tchatchoua, viny.
    Phone # +237691167590
    Email Id: Tchatchouaviny@yahoo.fr
    Portfolio: assouviny.com.

    Warm Regards,
    TatfoMarket Store

    """
    print("\n\n")
    print(message,"\n")
    from_email = settings.EMAIL_HOST_USER 
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

def account_verify(request, token):
	pf = Verification.objects.filter(token=token).first()
	pf.verify = True
	pf.save()
	messages.success(request, "Your Account has been Verified, You can Login Now.")
	return redirect('accountss:login')  