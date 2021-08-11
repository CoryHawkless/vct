from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
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
        'email': fields.String(required=True, description='user email address'),
        'name': fields.String(required=True, description='user username'),
        'description': fields.String(required=True, description='user password'),
        'deleted': fields.String(description='user Identifier')
    })
