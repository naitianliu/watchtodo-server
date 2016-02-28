from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.functions.watch_helper import WatchHelper
from api.functions.update_helper import UpdateHelper
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
    obj_watch = WatchHelper(username)
    obj_watch.add_watcher(action_id, watchers)
    UpdateHelper(username).add_update(action_id, "1011", obj_watch.datetime_now)
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
    update_list = UpdateHelper(username).get_update_list(int(last_timestamp))
    res_dict = dict(
        watch_updated_info=watch_updated_info,
        update_list=update_list
    )
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def get_update_list(request):
    try:
        username = request.user.username
        last_timestamp = request.GET['timestamp']
        update_list = UpdateHelper(username).get_update_list(int(last_timestamp))
        res_dict = dict(update_list=update_list)
        return Response(data=res_dict, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)


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


def test_notification(request):
    from api.utils.notification_helper import NotificationHelper
    NotificationHelper("").test()
    res_dict = dict(success=True)
    return HttpResponse("OK")