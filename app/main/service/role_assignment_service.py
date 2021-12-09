import uuid
import datetime

import flask

from app.main import db
from app.main.model.role_assignment import RoleAssignment
from typing import Dict, Tuple


def save_new_role_assignment(request: flask.request) -> Tuple[Dict[str, str], int]:
    data=request.json
    # Validate that role_name, project_id and user_id are present in the request and they are valid integers or strings
    try:
        _role=data['role']
        _project_id=None if len(str(data['project_id']))==0 else data['project_id']
        _user_id=data['user_id']
    except:
        response_object = {
            'status': 'fail',
            'message': 'Required parameters invalid',
        }
        return response_object, 401

    try:
        is_num = None if len(str(data['project_id']))==0 else int(_project_id)
    except:
        response_object = {
            'status': 'fail',
            'message': 'Project ID supplied is not valid',
        }
        return response_object, 401
    try:
        is_num = int(_user_id)
    except:
        response_object = {
            'status': 'fail',
            'message': 'User ID supplied is not valid',
        }
        return response_object, 401

    #TODO: Validate that the user has 'admin' access on this project id

    try:
        existing_roles=RoleAssignment.query.filter_by(user_id=_user_id,project_id=_project_id,role=_role)
        if existing_roles.count()>0:
            response_object = {
                'status': 'fail',
                'message': 'Role already defined for this user\project',
            }
            return response_object, 409
    except:
        response_object = {
            'status': 'fail',
            'message': 'Error checking current roles for this user',
        }
        return response_object, 409

    try:
        print("{} {} {}".format(_user_id,_project_id,_role))
        new_role_assignment = RoleAssignment(
            user_id=_user_id,
            project_id=_project_id,
            role=_role
        )

        new_role_assignment.save()
        return new_role_assignment.to_dict(_hide=['project_id','user_id']),200
    except:
        response_object = {
            'status': 'fail',
            'message': 'New role assignment creation failed',
        }
        return response_object, 409


def get_roles_for_user(request: flask.request):
    # Pull the projectID from the request
    data = request.json
    project_id=data['project_id']
    user_id=data['user_id']
    roles=RoleAssignment.query.filter_by(user_id=user_id,project_id=project_id).all()
    roles_list=[]
    for _role in roles:
        roles_list.append(_role.role)

    response_object = {
        'status': 'success',
        'message': 'Roles for user' + str(roles_list),
    }
    return response_object, 409








def save_changes(data: RoleAssignment) -> None:
    db.session.add(data)
    db.session.commit()

