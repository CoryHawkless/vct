from .. import db
from ..util import commonModelAttributes
from sqlalchemy.ext.declarative import declared_attr

class RoleAssignment(db.Model,commonModelAttributes.CommonModelAttributes):
    """ RoleAssignment Model for storing volume related details """
    __tablename__ = "role_assignments"

    user_id =                   db.Column(db.Integer, db.ForeignKey('user.id'),
                                    nullable=False)
    role =                      db.Column(db.String(256),nullable=False)
    active =                      db.Column(db.Boolean(),nullable=False,default=True)
    project_id =                db.Column(db.Integer, db.ForeignKey('projects.id'),
                                    nullable=False)

    def __repr__(self):
        return "<RoleAssignment '{}'>".format(self.id)

    @declared_attr
    def project(cls):
        return db.relationship(
            'Project',
            primaryjoin='Project.id == %s.project_id' % cls.__name__,
            remote_side='Project.id'
        )

    @declared_attr
    def user(cls):
        return db.relationship(
            'User',
            primaryjoin='User.id == %s.user_id' % cls.__name__,
            remote_side='User.id'
        )