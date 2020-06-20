from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Product, CustomField, CustomProductField

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')

class CustomFieldSerializer(serializers.ModelSerializer):
	owner = UserProfileSerializer(read_only=True)
	class Meta:
		model = CustomField
		fields = ('id', 'owner', 'name')

	def create(self, validated_data):
		instance = CustomField(**validated_data)
		owner = self.context['request'].user
		instance.owner = owner
		instance.save()
		return instance


class CustomProductFieldSerializer(serializers.ModelSerializer):
	custom_field_name = serializers.SerializerMethodField()
	class Meta:
		model = CustomProductField
		fields = ('id', 'product', 'custom_field', 'custom_field_name', 'value')

	def get_custom_field_name(self, obj):
		return obj.custom_field.name

	def create(self, validated_data):
		instance = CustomProductField(**validated_data)

		instance, created = CustomProductField.objects.get_or_create(
        	product=validated_data.get('product', None),
        	custom_field=validated_data.get('custom_field', None)
        )

		instance.value = validated_data.get('value', None)
		instance.save()
		return instance


class ProductSerializer(serializers.ModelSerializer):
	owner = UserProfileSerializer(read_only=True)
	custom_product_fields = CustomProductFieldSerializer(read_only=True, many=True)
	class Meta:
		model = Product
		fields = ('id', 'owner', 'title', 'price', 'description', 'custom_product_fields')

	def create(self, validated_data):
		instance = Product(**validated_data)
		owner = self.context['request'].user
		instance.owner = owner
		instance.save()
		return instance


