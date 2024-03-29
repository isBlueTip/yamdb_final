import uuid

from django.core.mail import send_mail
from django.core.validators import MaxValueValidator
from django.utils import timezone
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import ADMIN_EMAIL


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'


def send_otp(email):
    key = uuid.uuid4().hex
    send_mail(
        'Регистрация нового пользователя',
        f'Ваш код подтверждения: {key}.'
        'Используйте его для авторизации.',
        ADMIN_EMAIL,  # 'from' field
        [email],  # 'to' field
        fail_silently=False,
    )
    return key


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token),
    }


def current_year():
    """Определение текущего года."""
    return timezone.now().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
