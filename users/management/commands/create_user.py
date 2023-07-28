from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс - команда для создания пользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='vas@vas.ru',
            first_name='vas',
            # last_name='django',
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )

        user.set_password('0112')

        user.save()
