from api.models import Comment
import datetime


class CommentHelper(object):
    def __init__(self, username, action_id=None, comment_id=None):
        self.username = username
        self.action_id = action_id
        self.comment_id = comment_id

    def add_comment(self, message, timestamp):
        if self.comment_id and self.action_id:
            Comment.objects.update_or_create(
                comment_id=self.comment_id,
                action_id=self.action_id,
                username=self.username,
                message=message,
                timestamp=int(timestamp)
            )

    def get_comment_list(self):
        comment_list = []
        if self.action_id:
            for row in Comment.objects.filter(action_id=self.action_id):
                comment_list.append(dict(
                    comment_id=row.comment_id,
                    action_id=row.action_id,
                    username=row.username,
                    message=row.message,
                    timestamp=str(row.timestamp)
                ))
        return comment_list

    def get_single_comment(self):
        if self.comment_id:
            try:
                row = Comment.objects.get(comment_id=self.comment_id)
                comment_dict = dict(
                    comment_id=row.comment_id,
                    action_id=row.action_id,
                    username=row.username,
                    message=row.message,
                    timestamp=row.timestamp
                )
                return comment_dict
            except Comment.DoesNotExist:
                return None
        else:
            return None