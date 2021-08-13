from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_role_required
from ..util.dto import VolumeTypeDto
from ..service.volume_type_service import save_new_volume_type, get_all_volume_types, get_a_volume_type
from typing import Dict, Tuple

api = VolumeTypeDto.api
_volume_type = VolumeTypeDto.volume_type


@api.route('/volume_types')
class VolumeTypeList(Resource):
    @api.doc('list_of_registered_volume_types')
    # @admin_role_required
    @api.marshal_list_with(_volume_type, envelope='data')
    def get(self):
        """List all registered volumes"""
        return get_all_volume_types()

    @api.expect(_volume_type, validate=True)
    @api.response(201, 'Volume Type successfully created.')
    @api.doc('create a new volume type')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Volume Type"""
        data = request.json
        return save_new_volume_type(data=data)


@api.route('volume_types/<volume_type_id>')
@api.param('public_id', 'The Volume Type identifier')
@api.response(404, 'Volume Type not found.')
class Volume_Type(Resource):
    @api.doc('get a volume type')
    @api.marshal_with(_volume_type)
    def get(self, volume_type_id):
        """get a volume type given its identifier"""
        volume_type = get_a_volume_type(volume_type_id)
        if not volume_type:
            api.abort(404)
        else:
            return volume_type



