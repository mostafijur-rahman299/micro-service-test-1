from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "You must be a owner to edit this object"
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id