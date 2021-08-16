import json
from random import randrange

from app.main.model.volume_type import Volume_Type
from app.main.model.volume import Volume
from app.main.model.project import Project
from app.main import db,create_app




app = create_app('dev')


with app.app_context():
    # db.create_all()
    #
    # p=Project()
    # p.name="Project1"+str(randrange(1000))
    # p.save()
    #
    # vt = Volume_Type()
    # vt.name = "VT1"

    # print (vt.to_dict())
    # db.session.add(vt)
    # db.session.commit()
    # print (vt.to_dict())
    # print (vt.serialise())
    #
    #
    # single=Volume_Type.query.all()
    # print(single)
    # #
    v=Volume()
    v.name="Volume 1"
    v.name_on_disk="SBSP"
    v.project_id=5
    v.type_id=5
    print(v.save())
    print (v.project)
    print (v.to_dict())
    # #
    # # db.session.add(p)
    # db.session.add(vt)
    # db.session.add(v)

    #
    # single=Project.query.first()
    # single.created_at="2021-08-14 09:11:31"
    # print(json.dumps(single.serialise()))

    db.session.commit()