import uuid
import datetime

from app.main import db
from app.main.model.volume_type import Volume_Type
from typing import Dict, Tuple


def save_new_volume_type(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    volume_type = Volume_Type.query.filter_by(name=data['name']).first()
    if not volume_type:
        new_volume_type = Volume_Type(
            public_id=str(uuid.uuid4()),
            name=data['name'],
            created_at=datetime.datetime.utcnow()
        )
        save_changes(new_volume_type)
        return new_volume_type
    else:
        response_object = {
            'status': 'fail',
            'message': 'Volume_Type already exists. Please Log in.',
        }
        return response_object, 409


def get_all_volume_types():
    return Volume_Type.query.all()


def get_a_volume_type(public_id):
    return Volume_Type.query.filter_by(public_id=public_id).first()




def save_changes(data: Volume_Type) -> None:
    db.session.add(data)
    db.session.commit()

