import uuid
import datetime

from app.main import db
from app.main.model.project import Project
from typing import Dict, Tuple


def save_new_project(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    project = Project.query.filter_by(email=data['email']).first()
    if not project:
        new_project = Project(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            projectname=data['projectname'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_project)
        return new_project
    else:
        response_object = {
            'status': 'fail',
            'message': 'Project already exists. Please Log in.',
        }
        return response_object, 409


def get_all_projects():
    return Project.query.all()


def get_a_project(public_id):
    return Project.query.filter_by(public_id=public_id).first()




def save_changes(data: Project) -> None:
    db.session.add(data)
    db.session.commit()

