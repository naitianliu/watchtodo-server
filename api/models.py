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
    action_id = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.IntegerField()


class Watcher(models.Model):
    action_id = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=100)
    timestamp = models.IntegerField()
