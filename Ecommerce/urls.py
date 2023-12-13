from django.urls import path
from . import views
from .views import view_wishlist, add_to_wishlist, remove_from_wishlist
# view_cart, add_to_cart, remove_from_cart


# from .views import CreateStripeCheckoutSessionView

app_name = 'Ecommerce'

urlpatterns = [
    # path('/', include('Ecommerce.urls')),
    path('welcome/', views.welcome, name='welcome'),
    path('', views.index, name="home"),
    path('terms/', views.terms, name="terms"),
    #  path('', HomeView.as_view(), name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('charge/', views.charge, name='charge'),
    path('success/', views.success, name='success'),
    path('cancelled/', views.cancel, name='cancel'),
    path('order/', views.order, name='order'),
    # path('', views.product_list, name='product_list'),
    # path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    #  path('create/', views.order_create, name='order_create'),
    #  path('apply/', views.coupon_apply, name='apply'),

    # path('cart/', views.cart_detail, name='cart_detail'),
    # path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    # path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # path('cart/', view_cart, name='view_cart'),
    # path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    # path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

    path('wishlist/', view_wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),

    path('livraison/', views.choix_livraison, name='livraison'),
    # path('process_livraison/<int:product_id>/', views.process_livraison, name='process_livraison'),


    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.CartListView.as_view(), name='cart_list'),
    path('cart-quantity/<int:cart_id>/', views.modify_cart_quantity, name='cart_quantity'),
    path('delete-cart-item/<int:cart_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('config/', views.stripe_config),  # new
    path('create-checkout-session/', views.create_checkout_session), # new

    path('newsletter/', views.newsletter, name='newsletter'), # new
    # Paiement NotchPay
    path('process/', views.process, name='process'), # new

    #Search
    path('search/', views.search, name='search'), # new



    # path(
    #     "create-checkout-session/<int:pk>/",
    #     CreateStripeCheckoutSessionView.as_view(),
    #     name="create-checkout-session",
    # ),


] 

