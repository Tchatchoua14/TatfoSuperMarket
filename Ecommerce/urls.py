from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import view_wishlist, add_to_wishlist, remove_from_wishlist


app_name = 'Ecommerce'

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('', views.index, name="home"),
    path('terms/', views.terms, name="terms"),
    path('checkout/', views.checkout, name='checkout'),
    path('charge/', views.charge, name='charge'),
    path('success/', views.success, name='success'),
    path('cancelled/', views.cancel, name='cancel'),
    path('order/', views.order, name='order'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('wishlist/', view_wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),

    path('livraison/', views.choix_livraison, name='livraison'),
    # path('process_livraison/<int:product_id>/', views.process_livraison, name='process_livraison'),


    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.CartListView.as_view(), name='cart_list'),
    path('cart-quantity/<int:cart_id>/', views.modify_cart_quantity, name='cart_quantity'),
    path('delete-cart-item/<int:cart_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('create-checkout-session/', views.create_checkout_session, name='config1'), # new

    path('newsletter/', views.newsletter, name='newsletter'), # new
    # Paiement NotchPay
    path('process/', views.process, name='process'), # new

    path('paiement/', views.paiement, name='paiement'), # new

    #Search
    path('search/', views.search, name='search'), # new

    path('apply/', views.coupon_apply, name='apply'),

] 

