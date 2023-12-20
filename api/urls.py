from django.urls import path
from rest_framework import routers
from rest_framework.routers import SimpleRouter
from .views import ProductList, ProductDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import registration

router = routers.DefaultRouter()
router = SimpleRouter()
# router.urls

router.register('products', ProductList.as_view(), basename="products")

# urlpatterns = router.urls

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path("register/", registration, name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("developers/", DevelopperListView.as_view(), name="developer-list"),

]


