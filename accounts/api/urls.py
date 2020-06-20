from django.urls import path, include
from rest_framework import routers

from accounts.api.views import UserProfileViewset, ProductViewset, \
						CustomFieldViewset, CustomProductFieldViewset

router = routers.DefaultRouter()

router.register(r'userprofile', UserProfileViewset, basename='userprofile')
router.register(r'products', ProductViewset, basename='products')
router.register(r'custom_fields', CustomFieldViewset, basename='custom_fields')
router.register(r'custom_product_fields', CustomProductFieldViewset, basename='custom_product_fields')

urlpatterns = [
	path('', include((router.urls, 'accounts'), namespace='accounts_api')),
	path('', include((router.urls, 'products'), namespace='products_api')),
	path('', include((router.urls, 'custom_fields'), namespace='custom_fields_api')),
	path('', include((router.urls, 'custom_product_fields'), namespace='custom_product_fields_api')),
]