from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='User related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })

class AuthDto:
    api = Namespace('auth', description='Authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class ProjectDto:
    api = Namespace('project', description='Project related operations')
    project = api.model('project', {
        'id': fields.Integer(description='Project ID'),
        'status': fields.String(description='Project status'),
        'created_at': fields.DateTime(description='Created Timestamp'),
        'deleted_at': fields.DateTime(description='Deleted Timestamp'),
        'name': fields.String(required=True, description='Volume Type name'),
        'description': fields.String(required=True, description='Description'),
    })

class VolumeDto:
    api = Namespace('volumes', description='Volume related operations')
    volume = api.model('volume', {
        'created_at': fields.DateTime(description='Created Timestamp'),
        'deleted_at': fields.DateTime(description='Deleted Timestamp'),
        'name': fields.String(required=True, description='Volume name'),
        'size': fields.Integer(required=True, description='Volume Size'),
        'description': fields.String(required=True, description='Optional description'),
        'type_id': fields.Integer(required=True, description='Volume Type ID'),
        'project_id': fields.Integer(required=True, description='Project ID'),

    })
    
class NetworkDto:
    api = Namespace('networks', description='Network related operations')
    network = api.model('network', {
        'id': fields.Integer(required=True, description='Project ID'),
        'created_at': fields.DateTime(description='Created Timestamp'),
        'deleted_at': fields.DateTime(description='Deleted Timestamp'),
        'name': fields.String(required=True, description='Network name'),
        'description': fields.String(required=True, description='Optional description'),
        'sementation_id': fields.Integer(required=True, description='Network Segmentation ID'),
        'project_id': fields.Integer(required=True, description='Project ID'),

    })

class VolumeTypeDto:
    api = Namespace('volume_types', description='Volume Types related operations')
    volume_type = api.model('volume_type', {
        'id': fields.Integer(required=True, description='Project ID'),
        'created_at': fields.DateTime(description='Created Timestamp'),
        'deleted_at': fields.DateTime(description='Deleted Timestamp'),
        'name': fields.String(required=True, description='Volume Type name'),
    })

class RoleAssignmentDto:
    api = Namespace('role_asignment', description='Roles assigned to users')
    role_assignment = api.model('role_asignment', {
        'id': fields.Integer(required=True, description='Project ID'),
        'created_at': fields.DateTime(description='Created Timestamp',read_only=True),
        'deleted_at': fields.DateTime(description='Deleted Timestamp'),
        'role_name': fields.String(required=True, description='Text based role name'),
        'project_id': fields.Integer(required=True, description='Project ID'),
    })