import json
from random import randrange

from app.main.model.volume_type import Volume_Type
from app.main.model.volume import Volume
from app.main.model.project import Project
from app.main import db, create_app

app = create_app('dev')
x="1a"




with app.app_context():
    query=Volume.query.filter_by(id=15)
    x=query.count()

    query1 = Volume.query.filter_by(id=5)
    y = query1.count()

    if query1.count():
        print(query1.first().to_dict())
    else:
        pass