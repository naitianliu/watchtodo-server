from django.contrib import admin

# Register your models here.

from register.models import UserInfo
from register.models import Friend

admin.site.register(UserInfo)
admin.site.register(Friend)