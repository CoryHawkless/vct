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

    project=Project.query.filter_by(id=5).first()
    print(project)

    # newRA=RoleAssignment()
    # newRA.user=cory
    # newRA.project=project
    # newRA.role="operator"
    # newRA.save()
    #
    # allRAs=RoleAssignment.query.filter_by(user=cory).all()
    # print(allRAs)
    new_role_assignment = RoleAssignment(
        user_id=1,
        project_id=4,
        role="god"
    )

    new_role_assignment.save()
    print(new_role_assignment.to_dict())