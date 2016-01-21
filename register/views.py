from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from register.signup.signup_by_email import SignupByEmail
from register.utils.token_helper import TokenHelper
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.authtoken.models import Token

# Create your views here.


@api_view(['POST'])
def register(request):
    post_data = json.loads(request.body)
    email = post_data['username']
    password = post_data['password']
    nickname = post_data['nickname']
    success = SignupByEmail().signup(email, password, nickname)
    res_dict = dict(
        success=success,
    )
    if success:
        token = TokenHelper().generate_token(username=email)
        res_dict['token'] = token
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
def login(request):
    post_data = json.loads(request.body)
    username = post_data['username']
    password = post_data['password']
    user_obj = auth.authenticate(username=username, password=password)
    if user_obj:
        user = User.objects.get(username=username)
        user.backend = "django.contrib.auth.backends.ModelBackend"
        auth.login(request, user)
        res_dict = dict(
            user_exists=True,
            token=Token.objects.get_or_create(user=user)[0].key,
            nickname=SignupByEmail().get_nickname_by_username(username)
        )
    else:
        res_dict = dict(
            user_exists=False
        )
    return Response(data=res_dict, status=status.HTTP_200_OK)


@api_view(['GET'])
def logout(request):
    auth.logout(request)
    res_dict = dict(
        success=True
    )
    return Response(data=res_dict, status=status.HTTP_200_OK)