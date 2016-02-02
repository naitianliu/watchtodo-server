from api.models import Project


class ProjectHelper(object):
    def __init__(self, username):
        self.username = username

    def add_project(self, project_id, project_name):
        Project(
            project_id=project_id,
            project_name=project_name,
            username=self.username
        ).save()

    def remove_project(self, project_id):
        pass

    def get_all_projects(self):
        pass

    def initiate_default_projects_at_registration(self, default_projects):
        for project in default_projects:
            project_id = project["project_id"]
            project_name = project["project_name"]
            self.add_project(project_id, project_name)