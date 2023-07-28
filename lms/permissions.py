from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """Проверка, что пользователь - владелец"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
        # return False


class ReadOnly(BasePermission):
    """разрешат только чтение (GET, HEAD, OPTIONS)"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CoursePermissions(BasePermission):
    """
    Разрешает
    - для безопасных методов - для модератора и владельца-не-модератора
    - для прочих методов - для владельца
    """

    def has_object_permission(self, request, view, obj):
        if request.method.upper() in SAFE_METHODS:
            if request.user.is_staff: return True
            return request.user == obj.owner
        else:
            return request.user == obj.owner
