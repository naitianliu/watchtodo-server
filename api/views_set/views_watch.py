from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.functions.watch_helper import WatchHelper
from api.functions.query_updated_info import QueryUpdatedInfo
from api.utils.device_token_helper import DeviceTokenHelper
import json


@api_view(['POST'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def add_watchers(request):
    username = request.user.username
    post_data = json.loads(request.body)
    action_id = post_data["action_id"]
    watchers = post_data["watchers"]
    WatchHelper(username).add_watcher(action_id, watchers)
    res_dict = dict(success=True)
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def remove_watcher(request):
    username = request.user.username
    post_data = json.loads(request.body)
    action_id = post_data["action_id"]
    watcher = post_data["watcher"]
    WatchHelper(username).remove_watcher(action_id, watcher)
    res_dict = dict(success=True)
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def get_updated_watch_list(request):
    username = request.user.username
    last_timestamp = request.GET['timestamp']
    watch_updated_info = QueryUpdatedInfo(username, int(last_timestamp)).get_updated_watch_info()
    return Response(data=watch_updated_info, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def update_device_token(request):
    try:
        username = request.user.username
        post_data = json.loads(request.body)
        device_token = post_data["device_token"]
        DeviceTokenHelper(username).add_update_device_token(device_token)
        res_dict = dict(success=True)
        return Response(data=res_dict, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)