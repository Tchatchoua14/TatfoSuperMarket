from django.urls import path
from . import views

app_name = 'Ecommerce'

urlpatterns = [
    # path('/', include('Ecommerce.urls')),
    path('welcome', views.welcome, name='welcome'),
    path('', views.index, name="home"),
    path('terms', views.terms, name="terms"),
    #  path('', HomeView.as_view(), name='home'),
    # path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('', views.product_list, name='product_list'),
    # path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    #  path('create/', views.order_create, name='order_create'),
    #  path('apply/', views.coupon_apply, name='apply'),
]
