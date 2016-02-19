from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.functions.comment_helper import CommentHelper
from api.functions.watch_helper import WatchHelper
from api.utils.notification_helper import NotificationHelper
import json


@api_view(['GET'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def get_comment_list(request):
    username = request.user.username
    action_id = request.GET['action_id']
    comments = CommentHelper(username, action_id).get_comment_list()
    res_dict = dict(comments=comments)
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def add_comment(request):
    try:
        username = request.user.username
        post_data = json.loads(request.body)
        comment_id = post_data["comment_id"]
        action_id = post_data["action_id"]
        message = post_data["message"]
        timestamp = post_data["timestamp"]
        CommentHelper(username, action_id, comment_id).add_comment(message, timestamp)
        # send notification
        watchers = WatchHelper(username).get_watcher_list_by_action_id(action_id)
        payload_dict = dict(
            type="comment",
            action_id=action_id
        )
        for watcher in watchers:
            NotificationHelper(watcher).send_simple_notification(message, payload_dict=payload_dict)
        res_dict = dict(success=True)
        return Response(data=res_dict, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
