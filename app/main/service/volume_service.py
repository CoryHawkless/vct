import uuid
import datetime

from app.main import db
from app.main.model.volume import Volume
from typing import Dict, Tuple


def save_new_volume(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    volume = Volume.query.filter_by(email=data['email']).first()
    if not volume:
        new_volume = Volume(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            volumename=data['volumename'],
            password=data['password'],
            created_at=datetime.datetime.utcnow()
        )
        save_changes(new_volume)
        return (new_volume)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Volume already exists. Please Log in.',
        }
        return response_object, 409


def get_all_volumes():
    return Volume.query.all()


def get_a_volume(public_id):
    return Volume.query.filter_by(public_id=public_id).first()




def save_changes(data: Volume) -> None:
    db.session.add(data)
    db.session.commit()

