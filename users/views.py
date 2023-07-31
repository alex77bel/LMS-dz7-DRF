from rest_framework import viewsets
from users.models import User
from users.permissions import UserPermissions
from users.serializers import UserSerializerAll, UserSerializerShort


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [UserPermissions]

    def get_serializer_class(self, **kwargs):
        """
       Возвращает класс, который следует использовать для сериализатора.
       При этом при просмотре чужого профиля должна быть доступна только общая информация,
       урезанное число полей.
        """
        if self.action == 'retrieve':
            if self.request.user.pk == int(self.kwargs['pk']):
                return UserSerializerAll
            return UserSerializerShort
        return UserSerializerShort
