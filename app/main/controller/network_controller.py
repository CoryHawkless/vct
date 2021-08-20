import flask
from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required,role_required,project_id_required
from ..util.dto import NetworkDto
from ..service.network_service import save_new_network, get_all_networks, get_a_network
from typing import Dict, Tuple

api = NetworkDto.api
_network = NetworkDto.network



@api.route('/')
class NetworkList(Resource):
    @token_required
    @project_id_required
    @role_required(["list_all_networks","operator"])
    @api.doc('list_of_registered_networks')
    # @api.marshal_list_with(_network, envelope='data')
    def get(self):
        """List all registered networks
        Optional parameter=project_id
        """

        return flask.jsonify(get_all_networks(request))

    @token_required
    @role_required(["create_network"])
    @api.response(201, 'Network successfully created.')
    @api.doc('create a new network')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Network """
        return save_new_network(request)


@api.route('/<network_id>')
@api.param('network_id', 'The Network identifier')
@api.response(404, 'Network not found.')
@api.response(200, 'Network found.')
class Network(Resource):
    @token_required
    @api.doc('get a network')
    # @api.marshal_with(_network)
    def get(self, network_id):
        """Get a network given its identifier"""
        this_network = get_a_network(network_id)
        return this_network



