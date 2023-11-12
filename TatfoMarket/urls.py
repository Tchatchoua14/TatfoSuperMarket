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
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ecommerce.urls')),
    path('', include('account.urls')),
    # path('accounts/', include('account.urls')),
    # path('', include('allauth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    # path('social-auth/', include('social_django.urls', namespace='social')),
    #path('order/', include('order.urls', namespace='order')),
]

#handling the 404 error
handler404 = 'Ecommerce.views.error_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# github
# cle client 9e85d9492e25f149252b
# cle secret f190d24327ee5ffdc6063caf02b4590f9cf586ed 

# facebook 
# cle client 701820614848473
# cle secret  58ee2658c1903c398f2dc9c215a1111f

# google
# 574111392765-150nfpg6sn2dql8o0m78j2cfqduuu7an.apps.googleusercontent.com
# cle client 574111392765-150nfpg6sn2dql8o0m78j2cfqduuu7an.apps.googleusercontent.com
# cle secret  

#    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  vrai code secret
    # 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