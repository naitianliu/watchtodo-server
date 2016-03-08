from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from register.friends.friends_helper import FriendsHelper
from api.utils.notification_helper import NotificationHelper


@api_view(['GET'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def get_friend_list(request):
    try:
        username = request.user.username
        friend_list = FriendsHelper(username).get_friend_list_by_username()
        res_dict = dict(
            friend_list=friend_list
        )
        return Response(data=res_dict, status=status.HTTP_200_OK)
    except Exception as err:
        print("error: get_friend_list")
        print(err)


@api_view(['GET'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def get_user_list_by_keyword(request):
    try:
        username = request.user.username
        keyword = request.GET['keyword']
        res_dict = FriendsHelper(username).get_user_list_by_keyword(keyword)
        return Response(data=res_dict, status=status.HTTP_200_OK)
    except Exception as err:
        print(get_user_list_by_keyword)
        print(err)


@api_view(['GET'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def send_friend_request(request):
    username = request.user.username
    friend_username = request.GET['friend_username']
    FriendsHelper(username).send_friend_request(friend_username)
    message = "You received a friend invitation"
    payload_dict = dict(
        type="friend",
        subtype="send"
    )
    NotificationHelper(friend_username).send_simple_notification(message, payload_dict=payload_dict)
    res_dict = dict(
        result='success'
    )
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def accept_friend_request(request):
    username = request.user.username
    friend_username = request.GET['friend_username']
    FriendsHelper(username).accept_friend_request(friend_username)
    message = "Your invitation has been accepted"
    payload_dict = dict(
        type="friend",
        subtype="accept"
    )
    NotificationHelper(friend_username).send_simple_notification(message, payload_dict=payload_dict)
    res_dict = dict(
        result='success'
    )
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def get_pending_friend_request_list(request):
    username = request.user.username
    requester_list = FriendsHelper(username).get_pending_friend_request_list()
    res_dict = dict(
        requester_list=requester_list
    )
    return Response(data=res_dict, status=status.HTTP_200_OK)