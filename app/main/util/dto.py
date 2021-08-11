from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class ProjectDto:
    api = Namespace('project', description='Project related operations')
    project = api.model('project', {
        'name': fields.String(required=True, description='Name'),
        'description': fields.String(required=True, description='Description'),
        'id': fields.String(required=True, description='Project ID'),
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class VolumeDto:
    api = Namespace('volumes', description='Volume related operations')
    volume = api.model('volume', {
        'name': fields.String(required=True, description='user email address'),
        'size': fields.Integer(required=True, description='Volume Size'),
        'description': fields.String(required=True, description='Optional description'),
        'deleted': fields.Boolean(description='Deleted?')
    })


class VolumeTypeDto:
    api = Namespace('volume_types', description='Volume Types related operations')
    volume_type = api.model('volume_type', {

        'name': fields.String(required=True, description='Volume Type name'),
        'description': fields.String(required=True, description='Optional description'),
        'deleted': fields.Boolean(description='Deleted?')
    })
