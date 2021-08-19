from datetime import datetime

import flask

from app.main import db
from app.main.model.volume_type import Volume_Type
from typing import Dict, Tuple


def save_new_volume_type(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    # volume_type = Volume_Type.query.filter_by(name=data['name']).first()
    volume_type=False
    if not volume_type:
        new_volume_type = Volume_Type(
            name=data['name'],
            size=data['name'],
            created_at=datetime.datetime.utcnow()

        )
        new_volume_type.save()
        return flask.jsonify(new_volume_type.to_dict())
    else:
        response_object = {
            'status': 'fail',
            'message': 'Volume_Type already exists. Please Log in.',
        }
        return response_object, 409


def get_all_volume_types():
    return Volume_Type.query.all()


def get_a_volume_type(volume_type_id):
    try:
        is_num = int(volume_type_id)
    except:
        response_object = {
            'status': 'fail',
            'message': 'ID supplied is not valid',
        }
        return response_object, 401

    query= Volume_Type.query.filter_by(id=volume_type_id)
    if query.count()==1:
        return flask.jsonify(query.first().to_dict())
    else:
        response_object = {
            'status': 'fail',
            'message': 'Volume Type with this name ID does not exist',
        }
        return response_object, 404

def save_changes(data: Volume_Type):
    db.session.add(data)
    db.session.commit()

