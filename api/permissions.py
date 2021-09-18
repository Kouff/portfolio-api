from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, vacation_obj):
        return request.method in SAFE_METHODS or vacation_obj.owner_id == request.user.pk


class IsOwnerForImageOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, vacation_obj):
        return request.method in SAFE_METHODS or vacation_obj.portfolio.owner_id == request.user.pk


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, vacation_obj):
        return request.method in SAFE_METHODS or vacation_obj.author_id == request.user.pk
