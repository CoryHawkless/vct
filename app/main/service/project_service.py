import uuid
import datetime

from app.main import db
from app.main.model.project import Project
from typing import Dict, Tuple


def save_new_project(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    new_project = Project(
        id=str(uuid.uuid4()),
        name=data['name'],
        description=data['description'],
        created_at=datetime.datetime.utcnow()
    )
    save_changes(new_project)
    return new_project



def get_all_projects():
    return Project.query.all()


def get_a_project(public_id):
    return Project.query.filter_by(public_id=public_id).first()

def save_changes(data: Project) -> None:
    db.session.add(data)
    db.session.commit()

