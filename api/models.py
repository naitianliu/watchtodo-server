from django.db import models

# Create your models here.


class ActionItem(models.Model):
    action_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    pending = models.BooleanField(default=True)
    updated_time = models.IntegerField()
    status = models.IntegerField()
    info = models.TextField()

    def __unicode__(self):
        return self.action_id


class Comment(models.Model):
    action_id = models.CharField(max_length=50)
    message = models.TextField()