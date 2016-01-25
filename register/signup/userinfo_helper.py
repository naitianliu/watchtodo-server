from register.models import UserInfo


class UserInfoHelper(object):
    def __init__(self):
        pass

    def get_user_info_by_username(self, username):
        try:
            obj = UserInfo.objects.get(username=username)
            user_info = dict(
                nickname=obj.nickname,
                username=obj.username,
                profile_img_url=obj.profile_img_url,
            )
        except UserInfo.DoesNotExist:
            user_info = dict()
        return user_info

    def get_user_info_list_by_username_list(self, username_list):
        user_info_list = []
        for row in UserInfo.objects.filter(username__in=username_list):
            user_info_list.append(dict(
                nickname=row.nickname,
                profile_img_url=row.profile_img_url,
                username=row.username
            ))
        return user_info_list