from django.urls import path, include
from rest_framework import routers

from accounts.api.views import UserProfileViewset

router = routers.DefaultRouter()
router.register(r'userprofile', UserProfileViewset)

urlpatterns = [
	path('', include((router.urls, 'accounts'), namespace='accounts_api')),
]