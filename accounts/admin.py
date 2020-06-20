from django.contrib import admin

from accounts.models import User, Product, CustomField, CustomProductField

model = [User, Product, CustomField, CustomProductField]

admin.site.register(model)
