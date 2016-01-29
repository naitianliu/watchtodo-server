import datetime


class WatchHelper(object):
    def __init__(self, username):
        self.username = username
        timestamp_str = datetime.datetime.now().strftime('%s')
        self.datetime_now = int(timestamp_str)

    def get_open_watch_list(self):
        pass

    def comment(self):
        pass

    def get_pending_comments(self):
        pass

    def get_new_watch_items(self):
        pass