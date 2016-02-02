from api.models import Comment
import datetime


class CommentHelper(object):
    def __init__(self, username, action_id):
        self.username = username
        self.action_id = action_id
        timestamp_str = datetime.datetime.now().strftime('%s')
        self.datetime_now = int(timestamp_str)

    def add_comment(self, message):
        Comment(
            action_id=self.action_id,
            username=self.username,
            message=message,
            timestamp=self.datetime_now
        ).save()

    def get_comment_list(self):
        comment_list = []
        for row in Comment.objects.filter(action_id=self.action_id):
            comment_list.append(dict(
                action_id=row.action_id,
                username=row.username,
                message=row.message,
                timestamp=row.timestamp
            ))
        return comment_list