from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, \
    IsAdminUser


# class IsOwnerOrStaff(BasePermission):
#     """Проверка, что пользователь - модератор или владелец"""
#
#     def has_permission(self, request, view):
#         if request.user.is_staff:
#             return True
#
#         return request.user == view.get_object().user


class IsOwner(BasePermission):
    """Проверка, что пользователь - владелец"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
        # return False


class ReadOnly(BasePermission):
    """разрешат только чтение (GET, HEAD, OPTIONS)"""

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
