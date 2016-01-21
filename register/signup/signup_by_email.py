from django.contrib.auth.models import User
from django.contrib import auth
from register.models import Nickname


class SignupByEmail(object):
    def __init__(self):
        pass

    def signup(self, email, password, nickname):
        username = email
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            user.save()
            self.__update_nickname(nickname, username)
            success = True
        except Exception as err:
            print(err)
            success = False
        return success

    def get_nickname_by_username(self, username):
        try:
            obj = Nickname.objects.get(username=username)
            nickname = obj.nickname
        except Nickname.DoesNotExist:
            nickname = ""
        return nickname

    def __update_nickname(self, nickname, username):
        try:
            obj = Nickname.objects.get(username=username)
            obj.nickname = nickname
            obj.save()
        except Nickname.DoesNotExist:
            Nickname(
                nickname=nickname,
                username=username
            ).save()
