from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermissions(BasePermission):
    """
    Разрешает
    - просматривать - всем
    - редактировать - только владельцу или суперюзеру
    """

    def has_object_permission(self, request, view, obj):
        if request.method.upper() in SAFE_METHODS:
            return True
        else:
            return request.user == obj or request.user.is_superuser
