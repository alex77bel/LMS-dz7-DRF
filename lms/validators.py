from rest_framework.exceptions import ValidationError


class VideoLinkValidator:
    """
    Класс валидации поля video_link
    """
    ALLOWED_LINK = 'https://www.youtube.com/'

    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        value = dict(data).get(self.field)
        if self.ALLOWED_LINK not in value:
            raise ValidationError('Bad video link')
