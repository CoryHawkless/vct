from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_role_required
from ..util.dto import VolumeDto
from ..service.volume_service import save_new_volume, get_all_volumes, get_a_volume
from typing import Dict, Tuple

api = VolumeDto.api
_volume = VolumeDto.volume



@api.route('/')
class VolumeList(Resource):
    @api.doc('list_of_registered_volumes')

    # @admin_role_required
    @api.marshal_list_with(_volume, envelope='data')
    def get(self):
        """List all registered volumes"""
        return get_all_volumes()

    @api.expect(_volume, validate=True)
    @api.response(201, 'Volume successfully created.')
    @api.doc('create a new volume')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Volume """
        data = request.json
        return save_new_volume(data=data)


@api.route('/<volume_id>')
@api.param('volume_id', 'The Volume identifier')
@api.response(404, 'Volume not found.')
class Volume(Resource):
    @api.doc('get a volume')
    @api.marshal_with(_volume)
    def get(self, volume_id):
        """Get a volume given its identifier"""
        volume = get_a_volume(volume_id)
        if not volume:
            api.abort(404)
        else:
            return volume



