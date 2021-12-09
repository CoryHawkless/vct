import uuid
import datetime

import flask

from app.main import db
from app.main.model.project import Project
from app.main.model.role_assignment import RoleAssignment
from typing import Dict, Tuple


def save_new_project(data: Dict[str, str], user) -> Tuple[Dict[str, str], int]:
    new_project = Project(
        # id=str(uuid.uuid4()),
        name=data['name'],
        description=data['description'],
        status='Created',
        created_at=datetime.datetime.utcnow()
    )
    save_changes(new_project)
    # Define role for each and every user
    new_role = RoleAssignment(
        user_id=user.id,
        role='admin',
        created_at=datetime.datetime.utcnow(),
        project_id=new_project.id
    )
    save_changes(new_role)
    return new_project



def get_all_projects():
    return Project.query.all()


def get_a_project(project_id):
    try:
        is_num = int(project_id)
    except:
        response_object = {
            'status': 'fail',
            'message': 'ID supplied is not valid',
        }
        return response_object, 401

    query= Project.query.filter_by(id=project_id)
    if query.count()==1:
        return flask.jsonify(query.first().to_dict())
    else:
        response_object = {
            'status': 'fail',
            'message': 'Project with this name ID does not exist',
        }
        return response_object, 404

def save_changes(data: Project) -> None:
    db.session.add(data)
    db.session.commit()


def delete_a_project(project_id):
    try:
        is_num = int(project_id)
    except:
        response_object = {
            'status': 'fail',
            'message': 'ID supplied is not valid',
        }
        return response_object, 401

    query= Project.query.filter_by(id=project_id)
    if query.count()==1:
        query.first().deleted_at = datetime.datetime.utcnow()
        query.first().status = 'Deleted'
        db.session.commit()
        db.session.close()
        return query.first()
    else:
        return False

