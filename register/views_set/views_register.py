from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from register.signup.signup_by_email import SignupHelper
from register.utils.token_helper import TokenHelper
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.authtoken.models import Token
from api.functions.project_helper import ProjectHelper

# Create your views here.


@csrf_exempt
def register(request):
    post_data = json.loads(request.body)
    username = post_data['username']
    password = post_data['password']
    nickname = post_data['nickname']
    success = SignupHelper().signup(username, password, nickname)
    res_dict = dict(
        success=success,
    )
    if success:
        # initiate default project at registration
        ProjectHelper(username).initiate_default_projects_at_registration()
        token = TokenHelper().generate_token(username=username)
        res_dict['token'] = token
        res_dict['user_info'] = SignupHelper().get_user_info_by_username(username)
    return HttpResponse(json.dumps(res_dict), content_type="application/json")


@csrf_exempt
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
            user_info=SignupHelper().get_user_info_by_username(username)
        )
    else:
        res_dict = dict(
            user_exists=False
        )
    return HttpResponse(json.dumps(res_dict), content_type="application/json")


@api_view(['GET'])
def logout(request):
    auth.logout(request)
    res_dict = dict(
        success=True
    )
    return Response(data=res_dict, status=status.HTTP_200_OK)


def version(request):
    return HttpResponse("OK")