from django.db import models

# Create your models here.


class ActionItem(models.Model):
    action_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    pending = models.BooleanField(default=True)
    updated_time = models.IntegerField()
    info = models.TextField()


class Comment(models.Model):
    action_id = models.CharField(max_length=50)
    message = models.TextField()