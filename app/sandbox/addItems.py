from random import randrange

from app.main.model.volume_type import Volume_Type
from app.main.model.volume import Volume
from app.main.model.project import Project
from app.main import db,create_app




app = create_app('dev')


with app.app_context():
    db.create_all()

    p=Project()
    p.name="Project1"+str(randrange(1000))
    p.save()

    vt = Volume_Type()
    vt.name = "VT1"

    vt.save()


    single=Volume_Type.query.first()
    # print(single)
    #
    v=Volume()
    v.name="Volume 1"
    v.name_on_disk="SBSP"
    v.project_id=p.id
    v.type_id=vt.id
    print(v.save())
    print (v.project)
    print (v.type)
    #
    # # db.session.add(p)
    # db.session.add(vt)
    # db.session.add(v)
    db.session.commit()