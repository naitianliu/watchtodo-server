from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class TokenHelper(object):
    def __init__(self):
        pass

    def generate_token(self, username):
        user_obj = User.objects.get(username=username)
        token_str = Token.objects.get_or_create(user=user_obj)[0].key
        return token_str