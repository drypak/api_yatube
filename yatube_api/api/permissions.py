from rest_framework import permissions


class IsOwnerOrReadOnlyPermission(permissions.BasePermission):
    """
    Позволяет редактировать только автору поста
    для остальных пользователей только чтение
    """

    def has_object_permission(self, request, view, obj):
        """Проверка, является ли пользователь автором поста."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
