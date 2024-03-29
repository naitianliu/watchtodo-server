import datetime
from api.models import Watcher


class WatchHelper(object):
    def __init__(self, username):
        self.username = username
        timestamp_str = datetime.datetime.now().strftime('%s')
        self.datetime_now = int(timestamp_str)

    def get_watch_action_id_list(self):
        action_id_list = []
        for row in Watcher.objects.filter(username=self.username):
            action_id_list.append(row.action_id)
        return action_id_list

    def get_watcher_list_by_action_id(self, action_id):
        watcher_list = []
        for row in Watcher.objects.filter(action_id=action_id):
            watcher_list.append(row.username)
        return watcher_list

    def add_watcher(self, action_id, watchers):
        current_watchers = []
        for row in Watcher.objects.filter(action_id=action_id):
            username = row.username
            if username in watchers:
                current_watchers.append(username)
            else:
                row.delete()
        new_watchers = list(set(watchers) - set(current_watchers))
        for username in new_watchers:
            Watcher(
                action_id=action_id,
                username=username,
                timestamp=self.datetime_now
            ).save()

    def remove_watcher(self, action_id, watcher_username):
        try:
            row = Watcher.objects.filter(action_id=action_id, username=watcher_username)
            row.delete()
        except Watcher.DoesNotExist:
            pass
