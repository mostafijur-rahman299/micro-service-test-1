from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.api.permissions import IsOwner, IsProductOwner, IsCustomProductFieldOwner
from accounts.api.serializers import UserProfileSerializer, ProductSerializer, \
									CustomFieldSerializer, CustomProductFieldSerializer
from accounts.models import Product, CustomField, CustomProductField

User = get_user_model()


class UserProfileViewset(viewsets.ModelViewSet):
	serializer_class = UserProfileSerializer
	permission_classes = [IsOwner, permissions.IsAuthenticated]

	def get_queryset(self, *args, **kwargs):
		return User.objects.filter(id=self.request.user.id)


class ProductViewset(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	permission_classes = [IsProductOwner, permissions.IsAuthenticated]

	def get_queryset(self, *args, **kwargs):
		return Product.objects.filter(owner=self.request.user).order_by("-created_at")


class CustomFieldViewset(viewsets.ModelViewSet):
	serializer_class = CustomFieldSerializer
	permission_classes = [IsProductOwner, permissions.IsAuthenticated]

	def get_queryset(self, *args, **kwargs):
		return CustomField.objects.filter(owner=self.request.user)


class CustomProductFieldViewset(viewsets.ModelViewSet):
	serializer_class = CustomProductFieldSerializer
	permission_classes = [IsCustomProductFieldOwner, permissions.IsAuthenticated]

	def get_queryset(self, *args, **kwargs):
		return CustomProductField.objects.filter(product__owner=self.request.user)
