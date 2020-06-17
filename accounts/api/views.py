from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model

from accounts.api.permissions import IsOwner
from accounts.api.serializers import UserProfileSerializer



User = get_user_model()


class UserProfileViewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = [IsOwner, permissions.IsAuthenticated]
