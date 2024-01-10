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
from django.urls import path, include, re_path
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
# import debug_toolbar
from rest_framework_simplejwt.views import TokenObtainPairView #new
# from oauth2_provider import views as oauth2_views #new

# from rest_framework_swagger.views import get_swagger_view

# schema_view = get_swagger_view(title="Notes API")

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView #new


urlpatterns = [
    path('admin/', login_required(admin.site.urls)),
    # path('', include('Ecommerce.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    # path('social-auth/', include('social_django.urls', namespace='social')),
    # path('cookies/', include('cookie_law.urls')), #new
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #new
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('api.urls')),
    # path('api/v1', include('router.urls')),
    # path('api/docs/', schema_view), #new 
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')), #new
    # path('oauth2-info/', 'oauth2_views.AuthorizationEndpoint.as_view()', name='oauth2_info'), #new
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
