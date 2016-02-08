from api.functions.todo_list_helper import TodoListHelper
from api.functions.watch_helper import WatchHelper
from api.models import Comment
from api.models import ActionItem
from register.models import Friend
from register.signup.userinfo_helper import UserInfoHelper
import json


class QueryUpdatedInfo(object):
    def __init__(self, username, last_timestamp):
        self.username = username
        self.last_timestamp = last_timestamp

    def __get_updated_comments_by_actions(self, action_id_list):
        updated_comments = []
        for row in Comment.objects.filter(action_id__in=action_id_list, timestamp__gte=self.last_timestamp):
            updated_comments.append(dict(
                action_id=row.action_id,
                username=row.username,
                message=row.message,
                timestamp=row.timestamp
            ))
        return updated_comments

    def __get_updated_actions_by_actions(self, action_id_list):
        updated_actions = []
        for row in ActionItem.objects.filter(action_id__in=action_id_list, updated_time__gte=self.last_timestamp):
            updated_actions.append(dict(
                action_id=row.action_id,
                project_id=row.project_id,
                username=row.username,
                pending=row.pending,
                updated_time=row.updated_time,
                status=row.status,
                info=json.loads(row.info)
            ))
        return updated_actions

    def __get_updated_friends(self):
        updated_friends = []
        for row in Friend.objects.filter(updated_time__gte=self.last_timestamp, accepter=self.username, pending=True):
            updated_friends.append(dict(
                requester=UserInfoHelper().get_user_info_by_username(row.requester),
                accepter=UserInfoHelper().get_user_info_by_username(row.accepter),
                pending=row.pending,
                updated_time=row.updated_time,
            ))
        for row in Friend.objects.filter(updated_time__gte=self.last_timestamp, requester=self.username, pending=False):
            updated_friends.append(dict(
                requester=UserInfoHelper().get_user_info_by_username(row.requester),
                accepter=UserInfoHelper().get_user_info_by_username(row.accepter),
                pending=row.pending,
                updated_time=row.updated_time
            ))
        return updated_friends

    def updated_info(self):
        my_action_id_list = TodoListHelper(self.username).get_open_action_id_list()
        updated_actions_me = self.__get_updated_actions_by_actions(my_action_id_list)
        updated_comments_me = self.__get_updated_comments_by_actions(my_action_id_list)
        watch_action_id_list = WatchHelper(self.username).get_watch_action_id_list()
        updated_actions_watch = self.__get_updated_actions_by_actions(watch_action_id_list)
        updated_comments_watch = self.__get_updated_comments_by_actions(watch_action_id_list)
        updated_friends = self.__get_updated_friends()
        updated_info = dict(
            updated_actions_me=updated_actions_me,
            updated_comments_me=updated_comments_me,
            updated_actions_watch=updated_actions_watch,
            updated_comments_watch=updated_comments_watch,
            updated_friends=updated_friends
        )
        return updated_info

    def get_updated_watch_info(self):
        watch_action_id_list = WatchHelper(self.username).get_watch_action_id_list()
        updated_actions_watch = self.__get_updated_actions_by_actions(watch_action_id_list)
        updated_comments_watch = self.__get_updated_comments_by_actions(watch_action_id_list)
        updated_watch_info = dict(
            updated_actions_watch=updated_actions_watch,
            updated_comments_watch=updated_comments_watch
        )
        return updated_watch_info