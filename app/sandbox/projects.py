import json
from random import randrange

from app.main.model.volume_type import Volume_Type
from app.main.model.volume import Volume
from app.main.model.user import User
from app.main.model.project import Project
from app.main.model.role_assignment import RoleAssignment
from app.main import db, create_app

app = create_app('dev')




with app.app_context():
    this_users_roles=RoleAssignment.query.filter_by(user_id=1,project_id=1).all()
    # print(this_users_roles)
    print(Project.query.filter_by(name="admin").first().id)