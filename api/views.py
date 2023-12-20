from rest_framework import generics
from .serializers import ProductSerializer
from Ecommerce.models import Product
from django.shortcuts import render

# from django.http import JsonResponse
# from django.views import View 
# from oauth2_provider.views.mixins import OAuthLibMixin
# from oauth2_provider.models import AccesToken

# Create your views here.

from django.contrib.auth import get_user_model
from rest_framework import response, decorators, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class ProductList(generics.ListCreateAPIView):
    # authentication_classes = TokenAuthentication
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwner, ]
    # permission_classes = [IsOwner, IsAuthenticated]

    #  Ensure a user sees only own Note objects.
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Product.objects.filter(owner=user)
    #     raise PermissionDenied()

    # # Set user as owner of a Notes object.
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = TokenAuthentication
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsOwner, IsAuthenticated]
    # permission_classes = [IsAuthenticated]


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)

# class DevelopperListView(OAuthLibMixin, View):
#     def get(self, request):
#         if not request.user.is_authenticated:
#             return JsonResponse({'error': 'Unauthorized'}, status=401)

#     access_token = AccessToken.objects.get(token=request.auth)

#     developer = access_token.user
#     print(developer)
    # return JsonResponse({'developerx': 'developerdddddd'})
