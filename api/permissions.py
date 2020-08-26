from rest_framework import permissions

from .models import UserRole


class ReviewCommentPermissions(permissions.BasePermission):
    '''Права доступа для комментариев и отзывов'''
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return not request.user.is_anonymous()

        if request.method in ('PATCH', 'DELETE'):
            return (request.user == obj.author or
                    request.user.role == UserRole.ADMIN or
                    request.user.role == UserRole.MODERATOR)

        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class IsAdminOrSuperUser(permissions.BasePermission):
    '''Права доступа для администратора'''
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(request.user.is_staff or
                        request.user.role == UserRole.ADMIN)
        return False
