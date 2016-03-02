from django.db import models

# Create your models here.


class ActionItem(models.Model):
    action_id = models.CharField(max_length=50)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=100)
    pending = models.BooleanField(default=True)
    updated_time = models.IntegerField()
    status = models.IntegerField()
    info = models.TextField()

    def __unicode__(self):
        return self.action_id


class Project(models.Model):
    project_id = models.CharField(max_length=50)
    project_name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)


class Comment(models.Model):
    comment_id = models.CharField(max_length=50)
    action_id = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.IntegerField()


class Watcher(models.Model):
    action_id = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=100)
    timestamp = models.IntegerField()


class WatcherProject(models.Model):
    project_id = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=100)


class DeviceToken(models.Model):
    username = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    updated_time = models.IntegerField()

    def __unicode__(self):
        return self.username


class Update(models.Model):
    uuid = models.CharField(max_length=50)
    action_id = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    updated_by = models.CharField(max_length=200)
    timestamp = models.IntegerField()