from register.models import Friend
from register.models import UserInfo
from register.signup.userinfo_helper import UserInfoHelper
import datetime

# get friend list by user id
# get user list by keyword
# send friend request
# accept friend request
# get pending friend request list


class FriendsHelper(object):
    def __init__(self, username):
        timestamp_str = datetime.datetime.now().strftime('%s')
        self.datetime_now = int(timestamp_str)
        self.username = username

    def get_friend_list_by_username(self):
        username_list = []
        for friend in Friend.objects.filter(requester=self.username, pending=False):
            friend_username = friend.accepter
            username_list.append(friend_username)
        for friend in Friend.objects.filter(accepter=self.username, pending=False):
            friend_username = friend.requester
            username_list.append(friend_username)
        friend_list = UserInfoHelper().get_user_info_list_by_username_list(username_list)
        return friend_list

    def get_user_list_by_keyword(self, keyword):
        username_list_by_username = UserInfoHelper().get_user_info_list_by_username_list([keyword])
        username_list_by_nickname = []
        for row in UserInfo.objects.filter(username=keyword):
            username_list_by_username.append(row.username)
        for row in UserInfo.objects.filter(nickname=keyword):
            username_list_by_nickname.append(row.username)
        result_dict = dict(
            user_list_by_username=UserInfoHelper().get_user_info_list_by_username_list(username_list_by_username),
            user_list_by_nickname=UserInfoHelper().get_user_info_list_by_username_list(username_list_by_nickname)
        )
        return result_dict

    def send_friend_request(self, accepter):
        try:
            Friend.objects.get(requester=self.username, accepter=accepter)
        except Friend.DoesNotExist:
            Friend(requester=self.username, accepter=accepter, pending=True, updated_time=self.datetime_now).save()

    def accept_friend_request(self, requester):
        try:
            row = Friend.objects.get(requester=requester, accepter=self.username, pending=True)
            row.updated_time = self.datetime_now
            row.pending = False
            row.save()
        except Friend.DoesNotExist:
            pass

    def get_pending_friend_request_list(self):
        friend_username_list = []
        for row in Friend.objects.filter(accepter=self.username, pending=True):
            friend_username_list.append(row.username)
        requester_list = UserInfoHelper().get_user_info_list_by_username_list(friend_username_list)
        return requester_list