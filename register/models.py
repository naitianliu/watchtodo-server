from django.db import models

# Create your models here.


class Nickname(models.Model):
    nickname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nickname