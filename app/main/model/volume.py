from .. import db, flask_bcrypt
from ..util import commonModelAttributes
from sqlalchemy.ext.declarative import declared_attr


class Volume(db.Model,commonModelAttributes.CommonModelAttributes):
    """ Volume Model for storing volume related details """
    __tablename__ = "volumes"

    name =                      db.Column(db.String(128))
    description =               db.Column(db.String(256))
    type =                      db.Column(db.Integer, db.ForeignKey('volume_types.id'),
                                    nullable=False)
    size =                      db.Column(db.Integer,nullable=False,default=0)
    id_on_disk =               db.Column(db.String(256),nullable=False)
    project_id =                db.Column(db.Integer, db.ForeignKey('projects.id'),
                                    nullable=False)

    def __repr__(self):
        return "<Volume '{}'>".format(self.id)

    @declared_attr
    def project_name(cls):
        return db.relationship(
            'Project',
            primaryjoin='Project.id == %s.project_id' % cls.__name__,
            remote_side='Project.id'
        )