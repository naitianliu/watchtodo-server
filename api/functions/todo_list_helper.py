from api.models import ActionItem
import json
import datetime
from api.functions.update_helper import UpdateHelper


class TodoListHelper(object):
    def __init__(self, username):
        self.username = username
        timestamp_str = datetime.datetime.now().strftime('%s')
        self.datetime_now = int(timestamp_str)

    def get_todo_list(self, timestamp):
        todo_list = []
        for row in ActionItem.objects.filter(updated_time__gte=timestamp, username=self.username):
            todo_list.append(dict(
                action_id=row.action_id,
                username=row.username,
                status=row.status,
                updated_time=row.updated_time,
                info=json.loads(row.info)
            ))
        return todo_list

    def get_username_by_action_id(self, action_id):
        try:
            row = ActionItem.objects.get(action_id=action_id)
            username = row.username
        except ActionItem.DoesNotExist:
            username = None
        return username

    def get_open_action_id_list(self):
        action_id_list = []
        for row in ActionItem.objects.filter(username=self.username, status__in=["0", "1"]):
            action_id_list.append(row.action_id)
        return action_id_list

    def add_update_action_item(self, action_id, action_info):
        try:
            row = ActionItem.objects.get(action_id=action_id, username=self.username)
            row.info = json.dumps(action_info)
            row.updated_time = self.datetime_now
            row.save()
            UpdateHelper(self.username).add_update(action_id, "1004", self.datetime_now)
        except ActionItem.DoesNotExist:
            ActionItem(
                action_id=action_id,
                username=self.username,
                status="0",
                updated_time=self.datetime_now,
                info=json.dumps(action_info)
            ).save()
            UpdateHelper(self.username).add_update(action_id, "1001", self.datetime_now)

    def remove_action_item(self, action_id):
        try:
            row = ActionItem.objects.get(action_id=action_id, username=self.username)
            row.status = "3"
            row.updated_time = self.datetime_now
            row.save()
            success = True
        except ActionItem.DoesNotExist:
            success = False
        return success

    def update_status(self, action_id, status):
        try:
            row = ActionItem.objects.get(action_id=action_id, username=self.username)
            row.status = status
            row.updated_time = self.datetime_now
            row.save()
            success = True
        except ActionItem.DoesNotExist:
            success = False
        return success

    def complete(self, action_id):
        try:
            row = ActionItem.objects.get(action_id=action_id, username=self.username)
            row.status = "2"
            row.updated_time = self.datetime_now
            row.save()
            success = True
        except ActionItem.DoesNotExist:
            success = False
        return success