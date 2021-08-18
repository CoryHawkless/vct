import uuid
import datetime

import flask

from app.main import db
from app.main.model.volume import Volume
from typing import Dict, Tuple


def save_new_volume(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    # volume = Volume.query.filter_by(name=data['name']).first()
    volume=False
    if not volume:
        new_volume = Volume(
            name=data['name'],
            size=data['size'],
            description=data['description'],
            type_id=data['type_id'],
            name_on_disk="",
            project_id=data['project_id'],
        )
        # Validate the user has write access on this project

        # Validate the user has 'use' access on the volume type

        new_volume.save()
        return flask.jsonify(new_volume.to_dict())
    else:
        response_object = {
            'status': 'fail',
            'message': 'Volume with this name already exists.',
        }
        return response_object, 409


def get_all_volumes():
    return Volume.query.all()


def get_a_volume(public_id):
    try:
        is_num = int(public_id)
    except:
        response_object = {
            'status': 'fail',
            'message': 'ID supplied is not valid',
        }
        return response_object, 401

    query= Volume.query.filter_by(id=public_id)
    if query.count()==1:
        return flask.jsonify(query.first().to_dict())
    else:
        response_object = {
            'status': 'fail',
            'message': 'Volume with this name ID does not exist',
        }
        return response_object, 404





def save_changes(data: Volume) -> None:
    db.session.add(data)
    db.session.commit()

