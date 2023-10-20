from django.urls import path
from . import views

app_name = 'Ecommerce'

urlpatterns = [
    # path('/', include('Ecommerce.urls')),
    path('home', views.index, name="index"),
    #  path('', HomeView.as_view(), name='home'),
    # path('checkout/', CheckoutView.as_view(), name='checkout'),
]