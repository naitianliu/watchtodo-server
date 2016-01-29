from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.functions.todo_list_helper import TodoListHelper
import json


@api_view(['GET'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def get_todo_list(request):
    username = request.user.username
    timestamp_str = request.GET['timestamp']
    todo_list = TodoListHelper(username).get_todo_list(int(timestamp_str))
    res_dict = dict(todo_list=todo_list)
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def add_action(request):
    username = request.user.username
    post_data = json.loads(request.body)
    action_id = post_data["action_id"]
    action_info = post_data["action_info"]
    TodoListHelper(username).add_action_item(action_id, action_info)
    success = True
    res_dict = dict(result=success)
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def update_action(request):
    username = request.user.username
    post_data = json.loads(request.body)
    action_info = post_data["action_info"]
    action_id = post_data["action_id"]
    success = TodoListHelper(username).update_action_item(action_id, action_info)
    res_dict = dict(result=success)
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def remove_action(request):
    username = request.user.username
    post_data = json.loads(request.body)
    action_id = post_data["action_id"]
    success = TodoListHelper(username).remove_action_item(action_id)
    res_dict = dict(result=success)
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def update_status(request):
    try:
        username = request.user.username
        post_data = json.loads(request.body)
        action_id = post_data["action_id"]
        action_status = post_data["status"]
        success = TodoListHelper(username).update_status(action_id, action_status)
        res_dict = dict(result=success)
        return Response(data=res_dict, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)


@api_view(['POST'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def complete(request):
    username = request.user.username
    post_data = json.loads(request.body)
    action_id = post_data["action_id"]
    success = TodoListHelper(username).complete(action_id)
    res_dict = dict(result=success)
    return Response(data=res_dict, status=status.HTTP_200_OK)