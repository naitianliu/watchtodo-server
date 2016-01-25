from django.contrib.auth.models import User
from django.contrib import auth
from register.models import UserInfo


class SignupHelper(object):
    def __init__(self):
        pass

    def signup(self, username, password, nickname):
        try:
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
            self.__update_nickname(nickname, username)
            success = True
        except Exception as err:
            print(err)
            success = False
        return success

    def get_user_info_by_username(self, username):
        try:
            obj = UserInfo.objects.get(username=username)
            user_info = dict(
                username=obj.username,
                nickname=obj.nickname,
                profile_img_url=obj.profile_img_url
            )
        except UserInfo.DoesNotExist:
            user_info = dict()
        return user_info

    def __update_nickname(self, nickname, username):
        try:
            obj = UserInfo.objects.get(username=username)
            obj.nickname = nickname
            obj.save()
        except UserInfo.DoesNotExist:
            UserInfo(
                nickname=nickname,
                username=username
            ).save()

    def check_username(self, username):
        try:
            UserInfo.objects.get(username=username)
            is_valid = False
        except UserInfo.DoesNotExist:
            is_valid = True
        return is_valid