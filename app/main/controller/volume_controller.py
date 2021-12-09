import flask
from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required,role_required,project_id_required, specific_role_required_for_volume
from ..util.dto import VolumeDto
from ..service.volume_service import save_new_volume, get_all_volumes, get_a_volume, delete_a_volume, update_a_volume
from typing import Dict, Tuple

api = VolumeDto.api
_volume = VolumeDto.volume



@api.route('/')
class VolumeList(Resource):
    @token_required
    @project_id_required
    @role_required(["read_volumes"])
    @api.doc('list_of_registered_volumes')
    @api.marshal_list_with(_volume, envelope='data')
    def get(self):
        """List all registered volumes
        Optional parameter=project_id
        """

        return get_all_volumes(request)

    @token_required
    @role_required(["create_volume"])
    @api.expect(_volume, validate=True)
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
    @specific_role_required_for_volume(["read_volumes"])
    # @api.marshal_with(_volume)
    def get(self, volume_id):
        """Get a volume given its identifier"""
        this_volume = get_a_volume(volume_id)
        return this_volume

    @specific_role_required_for_volume(["delete_volume"])
    def delete(self, volume_id):
        """delete a volume given its identifier"""
        this_volume = delete_a_volume(volume_id)
        if this_volume:
            return {"project_id": this_volume.id, "name": this_volume.name, "description": this_volume.description,
                    "created_at": str(this_volume.created_at), "deleted_at": str(this_volume.deleted_at),
                    "status": this_volume.status, "size": this_volume.size}
        else:
            response_object = {
                'status': 'fail',
                'message': 'Volume with this name ID does not exist',
            }
            return response_object, 404

@api.route('/resize/<volume_id>')
@api.param('volume_id', 'The Volume identifier')
@api.response(404, 'Volume not found.')
@api.response(200, 'Volume found.')
class Volume(Resource):
    @token_required
    @api.doc('get a volume')
    @specific_role_required_for_volume(["resize_volume"])
    def post(self, volume_id):
        """resize a volume"""
        this_volume = update_a_volume(volume_id, request.json['size'])
        if this_volume == 'False1':
            response_object = {
                'status': 'fail',
                'message': 'The given size is smaller than original size',
            }
            return response_object, 500
        elif this_volume:
            return {"project_id": this_volume.id, "name": this_volume.name, "description": this_volume.description,
                    "created_at": str(this_volume.created_at), "deleted_at": str(this_volume.deleted_at),
                    "status": this_volume.status, "size": this_volume.size}
        else:
            response_object = {
                'status': 'fail',
                'message': 'Volume with this name ID does not exist',
            }
            return response_object, 404