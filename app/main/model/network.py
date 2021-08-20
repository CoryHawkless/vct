from .. import db
from ..util import commonModelAttributes
from sqlalchemy.ext.declarative import declared_attr


class Network(db.Model,commonModelAttributes.CommonModelAttributes):
    """ Network Model for storing network related details """
    __tablename__ = "networks"

    name =                      db.Column(db.String(128))
    description =               db.Column(db.String(256))
    segmentation_id =           db.Column(db.String(256))
    project_id =                db.Column(db.Integer, db.ForeignKey('projects.id'),
                                    nullable=False)


    def __repr__(self):
        return "<Network '{}'>".format(self.id)

    @declared_attr
    def project(cls):
        return db.relationship(
            'Project',
            primaryjoin='Project.id == %s.project_id' % cls.__name__,
            remote_side='Project.id'
        )
