"""
URL configuration for TatfoMarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required #new
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
# import debug_toolbar
from rest_framework_simplejwt.views import TokenObtainPairView #new
from oauth2_provider import views as oauth2_views #new

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView #new

admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('admin/', (admin.site.urls)),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #new
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('api.urls')),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')), #new
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), #new
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), #new
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns += i18n_patterns (
    path('', include('Ecommerce.urls')),
    path('', include('accountss.urls')),
)

#handling the 404 error
handler404 = 'Ecommerce.views.error_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += [
    #     path('__debug__/', include(debug_toolbar.urls)),
    # ]
