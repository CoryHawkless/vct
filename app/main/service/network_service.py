import uuid
import datetime

import flask

from app.main import db
from app.main.model.network import Network
from typing import Dict, Tuple


def save_new_network(request: flask.request) -> Tuple[Dict[str, str], int]:
    data=request.json
    # network = Network.query.filter_by(name=data['name']).first()
    network=False

    if not "description" in data:
        data['description']=""
    if not network:
        new_network = Network(
            name=data['name'],
            description=data['description'],
            project_id=data['project_id'],
            created_at=datetime.datetime.utcnow()
        )
        # Validate the user has write access on this project

        # Validate the user has 'use' access on the network type

        new_network.save()
        return flask.jsonify(new_network.to_dict(_hide=['project_id','type_id']))
    else:
        response_object = {
            'status': 'fail',
            'message': 'Network with this name already exists.',
        }
        return response_object, 409


def get_all_networks(request: flask.request):
    # Pull the projectID from the request
    data = request.json
    project_id=data['project_id']

    # Validate the projectID is a number
    try:
        is_num = int(project_id)
    except:
        response_object = {
            'status': 'fail',
            'message': 'Project ID supplied is not valid',
        }
        return response_object, 401

    # Check if the user has the list_all_networks role on this project ID

    # Query all networks by the specified projectID
    query= Network.query.filter_by(project_id=project_id)
    return_data=[]

    # Iterate through all objects and use the .to_dict function to normalise the response,
    # hiding project and network type for brevity
    for _network in query.all():
        return_data.append(_network.to_dict(_hide=['project']))

    return  return_data

def get_a_network(public_id):
    try:
        is_num = int(public_id)
    except:
        response_object = {
            'status': 'fail',
            'message': 'ID supplied is not valid',
        }
        return response_object, 401

    query= Network.query.filter_by(id=public_id)
    if query.count()==1:
        return flask.jsonify(query.first().to_dict())
    else:
        response_object = {
            'status': 'fail',
            'message': 'Network with this name ID does not exist',
        }
        return response_object, 404





def save_changes(data: Network) -> None:
    db.session.add(data)
    db.session.commit()

