from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.functions.comment_helper import CommentHelper
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
        action_id = post_data["action_id"]
        message = post_data["message"]
        CommentHelper(username, action_id).add_comment(message)
        res_dict = dict(success=True)
        return Response(data=res_dict, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
