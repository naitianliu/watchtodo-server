from api.models import ActionItem
import json
import datetime


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
                pending=row.pending,
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
        for row in ActionItem.objects.filter(username=self.username, pending=True):
            action_id_list.append(row.action_id)
        return action_id_list

    def add_action_item(self, action_id, action_info):
        ActionItem(
            action_id=action_id,
            username=self.username,
            pending=True,
            status=0,
            updated_time=self.datetime_now,
            info=json.dumps(action_info)
        ).save()

    def update_action_item(self, action_id, action_info):
        try:
            row = ActionItem.objects.get(action_id=action_id, username=self.username)
            row.info = json.dumps(action_info)
            row.save()
            success = True
        except ActionItem.DoesNotExist:
            success = False
        return success

    def remove_action_item(self, action_id):
        try:
            row = ActionItem.objects.get(action_id=action_id, username=self.username)
            row.delete()
            success = True
        except ActionItem.DoesNotExist:
            success = False
        return success

    def update_status(self, action_id, status):
        try:
            row = ActionItem.objects.get(action_id=action_id, username=self.username)
            row.status = int(status)
            row.updated_time = self.datetime_now
            row.save()
            success = True
        except ActionItem.DoesNotExist:
            success = False
        return success

    def complete(self, action_id):
        try:
            row = ActionItem.objects.get(action_id=action_id, username=self.username)
            row.status = 2
            row.pending = False
            row.updated_time = self.datetime_now
            row.save()
            success = True
        except ActionItem.DoesNotExist:
            success = False
        return success