from api.models import Update
from api.functions.watch_helper import WatchHelper
import uuid

MESSAGE_DICT = {
    "1001": "Creat a new action",
    "1002": "Start to take this action",
    "1003": "Complete this action",
    "1004": "Delete this action",
    "1005": "Update action content/property",
    "1011": "Add watchers",
    "1012": "Remove watchers",
}


class UpdateHelper(object):
    def __init__(self, username):
        self.username = username

    def add_update(self, action_id, update_code, timestamp):
        Update(
            uuid=uuid.uuid1(),
            action_id=action_id,
            code=update_code,
            updated_by=self.username,
            timestamp=timestamp
        ).save()

    def get_update_list(self, timestamp):
        update_list = []
        action_id_list = WatchHelper(self.username).get_watch_action_id_list()
        for row in Update.objects.filter(timestamp__gte=timestamp, action_id__in=action_id_list):
            code = row.code
            update_list.append(dict(
                uuid=row.uuid,
                action_id=row.action_id,
                code=code,
                message=MESSAGE_DICT[code],
                updated_by=row.updated_by,
                timestamp=str(row.timestamp)
            ))
        return update_list