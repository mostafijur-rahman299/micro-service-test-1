from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsProductOwner(permissions.BasePermission):
	
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsCustomProductFieldOwner(permissions.BasePermission):
	
    def has_object_permission(self, request, view, obj):
        return obj.product.owner == request.user