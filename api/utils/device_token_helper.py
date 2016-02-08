from api.models import DeviceToken
import datetime


class DeviceTokenHelper(object):
    def __init__(self, username):
        self.username = username
        timestamp_str = datetime.datetime.now().strftime('%s')
        self.datetime_now = int(timestamp_str)

    def add_update_device_token(self, device_token):
        try:
            row = DeviceToken.objects.get(username=self.username)
            row.device_token = device_token
            row.save()
        except DeviceToken.DoesNotExist:
            DeviceToken(
                username=self.username,
                device_token=device_token,
                updated_time=self.datetime_now
            ).save()