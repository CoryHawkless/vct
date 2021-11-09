from flask import request
from flask_restx import Resource
from app.main.util.decorator import admin_required, token_required,role_required,project_id_required
from app.main.util.dto import UserDto
from app.main.service.user_service import save_new_user, get_all_users, get_a_user
from typing import Dict, Tuple

api = UserDto.api
_user = UserDto.user

#TODO - Ensure that only admin users can list user accounts
@api.route('/')
class UserList(Resource):
    @admin_required
    # @role_required(["admin"])
    @api.doc('list_of_registered_users')
    # @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    # @api.doc('Create a new user')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new User"""
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user



