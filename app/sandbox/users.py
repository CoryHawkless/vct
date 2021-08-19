import json
from random import randrange

from app.main.model.volume_type import Volume_Type
from app.main.model.volume import Volume
from app.main.model.user import User
from app.main import db, create_app

app = create_app('dev')
x="1a"




with app.app_context():
    newUser=User()
    newUser.email="cory@hawkless.id.au"
    newUser.password="password"
    newUser.username="cory"
    newUser.admin=1
    newUser.save()