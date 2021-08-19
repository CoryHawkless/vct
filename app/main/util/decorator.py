from functools import wraps
from flask import request, abort
from app.main.service.auth_helper import Auth
from app.main.model.role_assignment import RoleAssignment
from typing import Callable


def token_required(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        user = Auth.get_logged_in_user(request)

        return f(*args, **kwargs)

    return decorated



def role_required(role):
    def decorated(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            data = request.json
            user = Auth.get_logged_in_user(request)
            print(user)
            project_id=data['project_id']
            print("This route requires user {} to have role '{}' on project #{}".format(user.username,role,project_id))
            this_users_roles=RoleAssignment.query.filter_by(user_id=user.id,project_id=project_id).all()

            role_found=False
            for this_role in this_users_roles:
                if this_role.role==role:
                    print("Role found :)")
                    role_found=True
            if not role_found:
                response="Permission Denied. You do not have the necessary role '" + str(role) + "' for project ID " +str(project_id)
                abort(401,response)

            return func(*args, **kwargs)
        return wrapper
    return decorated