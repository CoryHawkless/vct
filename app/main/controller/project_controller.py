from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_role_required
from ..util.dto import ProjectDto
from ..service.project_service import save_new_project, get_all_projects, get_a_project
from typing import Dict, Tuple

api = ProjectDto.api
_project = ProjectDto.project


@api.route('/')
class ProjectList(Resource):
    @api.doc('list_of_registered_projects')
    @admin_role_required
    @api.marshal_list_with(_project, envelope='data')
    def get(self):
        """List all registered projects"""
        return get_all_projects()

    @api.expect(_project, validate=True)
    @api.response(201, 'Project successfully created.')
    @api.doc('create a new project')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Project """
        data = request.json
        return save_new_project(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Project identifier')
@api.response(404, 'Project not found.')
class Project(Resource):
    @api.doc('get a project')
    @api.marshal_with(_project)
    def get(self, public_id):
        """get a project given its identifier"""
        project = get_a_project(public_id)
        if not project:
            api.abort(404)
        else:
            return project



