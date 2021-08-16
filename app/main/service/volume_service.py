import uuid
import datetime

import flask

from app.main import db
from app.main.model.volume import Volume
from typing import Dict, Tuple


def save_new_volume(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    volume = Volume.query.filter_by(name=data['name']).first()
    if not volume:
        new_volume = Volume(
            name=data['name'],
            size=data['size'],
            description=data['description'],
            type_id=data['type_id'],
            name_on_disk="",
            project_id=5,
        )

        new_volume.save()
        return flask.jsonify(new_volume.to_dict())
    else:
        response_object = {
            'status': 'fail',
            'message': 'Volume already exists. Please Log in.',
        }
        return response_object, 409


def get_all_volumes():
    return Volume.query.all()


def get_a_volume(public_id):
    return Volume.query.filter_by(id=public_id).first()




def save_changes(data: Volume) -> None:
    db.session.add(data)
    db.session.commit()

