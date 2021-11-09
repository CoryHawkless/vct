import uuid
import datetime

import flask

from app.main import db
from app.main.model.project import Project
from typing import Dict, Tuple


def save_new_project(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    new_project = Project(
        # id=str(uuid.uuid4()),
        name=data['name'],
        description=data['description'],
        created_at=datetime.datetime.utcnow()
    )
    save_changes(new_project)
    return flask.jsonify(new_project.to_dict())



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

