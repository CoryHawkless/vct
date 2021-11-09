import flask
from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required,role_required,user_id_required
from ..util.dto import RoleAssignmentDto
from ..service.role_assignment_service import get_roles_for_user,save_new_role_assignment
from typing import Dict, Tuple

api = RoleAssignmentDto.api
_role_assignment = RoleAssignmentDto.role_assignment


#TODO - Adjust the url to be role_assignments/userid/ and not require the userid in the body of the request
@api.route('/<user_id>')
class RoleAssignmentListForUser(Resource):
    @token_required
    # @user_id_required
    @role_required(["admin"])
    def get(self):
        """List all role assignments for specified user
        Required parameter=user_id
        """
        #TODO: Build a nice wrapper to allow functiosn to return a status code
        #TODO: Build a wrapper to return responses in a consistent format, eg, always has a sucess, fail
        response,code=get_roles_for_user(request)
        return flask.jsonify(response)

    @token_required
    @role_required(["admin"])
    @api.response(201, 'Role assigned successfully')
    @api.doc('create a new role assignment')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Role Assignment """
        response=save_new_role_assignment(request)
        return flask.jsonify(response)


