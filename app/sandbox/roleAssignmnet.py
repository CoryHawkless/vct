import json
from random import randrange


from app.main.model.role_assignment import RoleAssignment
from app.main.model.user import User
from app.main.model.project import Project


from app.main import db, create_app

app = create_app('dev')
x="1a"




with app.app_context():
    cory=User.query.filter_by(email="cory@hawkless.id.au").first()
    print (cory)

    project=Project.query.filter_by(id=4).first()
    print(project)

    newRA=RoleAssignment()
    newRA.user=cory
    newRA.project=project
    newRA.role="create_volume"
    newRA.save()

    allRAs=RoleAssignment.query.filter_by(user=cory).all()
    print(allRAs)