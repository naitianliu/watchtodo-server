from django.http import HttpResponse
from django.shortcuts import render
from api.utils.notification_helper import NotificationHelper
# Create your views here.


def test_notification(request):
    device_token = "DF6E74FEA570D2D65A6B5C9526528221B7D7F11C4DB496917A3F19D5642E3BF1"
    message = "test"
    payload = {}
    NotificationHelper([device_token]).send_notification_with_payload(message, payload)
    return HttpResponse("OK")