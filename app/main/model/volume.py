from .. import db, flask_bcrypt
from ..util import commonModelAttributes
from sqlalchemy.ext.declarative import declared_attr


class Volume(db.Model,commonModelAttributes.CommonModelAttributes):
    """ Volume Model for storing volume related details """
    __tablename__ = "volumes"

    name =                      db.Column(db.String(128))
    description =               db.Column(db.String(256))
    type_id =                   db.Column(db.Integer, db.ForeignKey('volume_types.id'),
                                    nullable=False)
    size =                      db.Column(db.Integer,nullable=False,default=0)
    name_on_disk =              db.Column(db.String(256),nullable=False)
    project_id =                db.Column(db.Integer, db.ForeignKey('projects.id'),
                                    nullable=False)


    def __repr__(self):
        return "<Volume '{}'>".format(self.id)

    @declared_attr
    def project(cls):
        return db.relationship(
            'Project',
            primaryjoin='Project.id == %s.project_id' % cls.__name__,
            remote_side='Project.id'
        )

    @declared_attr
    def volume_type(cls):
        return db.relationship(
            'Volume_Type',
            primaryjoin='Volume_Type.id == %s.type_id' % cls.__name__,
            remote_side='Volume_Type.id'
        )