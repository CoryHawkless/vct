from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.volume_controller import api as volume_ns
from .main.controller.volume_type_controller import api as volume_type_ns
from .main.controller.project_controller import api as project_ns
from .main.controller.role_assignment_controller import api as role_assignment_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='newStack API',
    version='0.1a',
    description='An API for all the IaaS automation and orchestration',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(project_ns, path='/project')
api.add_namespace(volume_ns, path='/volume')
api.add_namespace(volume_type_ns, path='/volume_type')
api.add_namespace(role_assignment_ns, path='/role_assignment')
api.add_namespace(auth_ns)
