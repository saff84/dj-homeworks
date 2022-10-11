from rest_framework.permissions import BasePermission


class IsAdvertisementOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and obj.creator == request.user:
            return True
        return bool(request.user and request.user.is_staff)
