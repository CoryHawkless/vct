from flask import request
from flask_restx import Resource

from ..util.dto import ProjectDto
from ..service.project_service import save_new_project, get_all_projects, get_a_project
from typing import Dict, Tuple

api = ProjectDto.api
_project = ProjectDto.project


@api.route('/')
class ProjectList(Resource):
    @api.doc('list_of_registered_projects')
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


