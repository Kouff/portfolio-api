from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, vacation_obj):
        return request.method in SAFE_METHODS or vacation_obj.owner_id == request.user.pk