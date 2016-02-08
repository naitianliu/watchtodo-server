from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    profile_img_url = models.TextField()
    login_type = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s - %s" % (self.user_id, self.username)


class Friend(models.Model):
    requester = models.CharField(max_length=200)
    accepter = models.CharField(max_length=200)
    pending = models.BooleanField(default=True)
    updated_time = models.IntegerField()

    def __unicode__(self):
        return self.requester
