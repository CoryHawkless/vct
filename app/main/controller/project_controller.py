from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required,role_required,project_id_required, project_role_required
from ..util.dto import ProjectDto
from ..service.project_service import save_new_project, get_all_projects, get_a_project, delete_a_project
from typing import Dict, Tuple
from app.main.service.auth_helper import Auth

api = ProjectDto.api
_project = ProjectDto.project


@api.route('/')
class ProjectList(Resource):
    @token_required
    @api.doc('list_of_registered_projects')
    @api.marshal_list_with(_project, envelope='data')
    def get(self):
        """List all registered projects"""
        data = get_all_projects()
        return [{"id":i.id, "name":i.name, "description":i.description, "status":i.status,
                 "created_at": i.created_at, "deleted_at": i.deleted_at} for i in data]

    @api.expect(_project, validate=True)
    @token_required
    @project_role_required(["admin"])
    @api.response(201, 'Project successfully created.')
    @api.doc('create a new project')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Project """
        data = request.json
        user = Auth.get_logged_in_user(request)
        project_status = save_new_project(data=data, user=user)
        return {"project_id": project_status.id, "name": project_status.name, "description": project_status.description}


@api.route('/<project_id>')
@api.param('project_id', 'The Project identifier')
@api.response(404, 'Project not found.')
class Project(Resource):
    @api.doc('Get a project')
    # @api.marshal_with(_project)
    def get(self, project_id):
        """get a project given its identifier"""
        this_project = get_a_project(project_id)
        return this_project

    @token_required
    @project_role_required(["delete_project"])
    def delete(self, project_id):
        """delete a project given its identifier"""

        this_project = delete_a_project(project_id)
        if this_project:
            return {"project_id": this_project.id, "name": this_project.name, "description": this_project.description,
                    "created_at": str(this_project.created_at), "deleted_at": str(this_project.deleted_at),
                    "status": this_project.status}
        else:
            response_object = {
                'status': 'fail',
                'message': 'Project with this name ID does not exist',
            }
            return response_object, 404

