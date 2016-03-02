from api.models import Project
from api.models import WatcherProject
import uuid

DEFAULT_PROJECTS = ["Personal", "Family", "Work", "Shopping", "Books to read", "Movies to watch"]


class ProjectHelper(object):
    def __init__(self, username):
        self.username = username

    def add_project(self, project_name):
        project_id = uuid.uuid1()
        Project(
            project_id=project_id,
            project_name=project_name,
            username=self.username
        ).save()
        return project_id

    def add_watchers_into_project(self, project_id, watchers):
        object_list = []
        for watcher_username in watchers:
            object_list.append(WatcherProject(
                project_id=project_id,
                username=watcher_username
            ))
        WatcherProject.objects.bulk_create(object_list)

    def remove_project(self, project_id):
        pass

    def get_all_projects(self):
        projects = []
        for row in Project.objects.filter(username=self.username):
            project_id = row.project_id
            project_name = row.project_name
            watchers = self.__get_watchers_by_project_id(project_id=project_id)
            projects.append(dict(
                project_id=project_id,
                project_name=project_name,
                watchers=watchers
            ))
        return projects

    def __get_watchers_by_project_id(self, project_id):
        watchers = []
        for row in WatcherProject.objects.filter(project_id=project_id):
            watchers.append(row.username)
        return watchers

    def initiate_default_projects_at_registration(self):
        for project_name in DEFAULT_PROJECTS:
            self.add_project(project_name)