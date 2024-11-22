from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class EmailBackend:
    """
    Autenticação com base no e-mail.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # Usando email como username
            if user.check_password(password):
                return user
        except ObjectDoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
