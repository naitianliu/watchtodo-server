from apns import APNs, Frame, Payload, PayloadAlert
from watchtodo.settings import BASE_DIR
from api.utils.device_token_helper import DeviceTokenHelper
import time


class NotificationHelper(object):
    def __init__(self, username):
        self.cert_path = BASE_DIR + '/certs/APNCert.pem'
        self.key_path = BASE_DIR + '/certs/APNKey.pem'
        self.device_token = DeviceTokenHelper(username).get_device_token()

    def send_simple_notification(self, message, payload_dict):
        apns = APNs(use_sandbox=True, cert_file=self.cert_path, key_file=self.key_path)
        payload = Payload(alert=message, sound="default", badge=1, custom=payload_dict)
        apns.gateway_server.send_notification(self.device_token, payload)
        apns.gateway_server.register_response_listener(self.__response_listener)

    def send_notification_with_custom_button(self, message, button_title):
        apns = APNs(use_sandbox=True, cert_file=self.cert_path, key_file=self.key_path)
        alert = PayloadAlert(message, action_loc_key=button_title)
        payload = Payload(alert=alert, sound="default")
        apns.gateway_server.send_notification(self.device_token, payload)
        apns.gateway_server.register_response_listener(self.__response_listener)

    def __response_listener(self, error_response):
        print("client get error-response: " + str(error_response))

    '''
    def send_notification_with_payload(self, message, payload_dict):
        if self.device_token_list:
            apns = APNs(use_sandbox=True, cert_file=self.cert_path, key_file=self.key_path)
            frame = Frame()
            identifier = 1
            expiry = int(time.time()) + 3600
            priority = 10
            payload = Payload(alert=message, sound="default", badge=1, custom=payload_dict)
            for device_token in self.device_token_list:
                frame.add_item(device_token, payload, identifier, expiry, priority)
            apns.gateway_server.send_notification_multiple(frame)
    '''