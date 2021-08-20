import flask
from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required,role_required,project_id_required
from ..util.dto import VolumeDto
from ..service.volume_service import save_new_volume, get_all_volumes, get_a_volume
from typing import Dict, Tuple

api = VolumeDto.api
_volume = VolumeDto.volume



@api.route('/')
class VolumeList(Resource):
    @token_required
    @project_id_required
    @role_required(["list_all_volumes","operator"])
    @api.doc('list_of_registered_volumes')
    # @api.marshal_list_with(_volume, envelope='data')
    def get(self):
        """List all registered volumes
        Optional parameter=project_id
        """
        return flask.jsonify(get_all_volumes(request))

    @token_required
    @role_required(["create_volume"])
    @api.response(201, 'Volume successfully created.')
    @api.doc('create a new volume')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Volume """
        return save_new_volume(request)


@api.route('/<volume_id>')
@api.param('volume_id', 'The Volume identifier')
@api.response(404, 'Volume not found.')
@api.response(200, 'Volume found.')
class Volume(Resource):
    @token_required
    @api.doc('get a volume')
    # @api.marshal_with(_volume)
    def get(self, volume_id):
        """Get a volume given its identifier"""
        this_volume = get_a_volume(volume_id)
        return this_volume



