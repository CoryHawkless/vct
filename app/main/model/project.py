
from .. import db, flask_bcrypt
from ..util import commonModelAttributes


class Project(db.Model,commonModelAttributes.CommonModelAttributes):
    """ Project Model for storing project related details """
    __tablename__ = "projects"

    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=True)
    status = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return "<Project '{}'>".format(self.id)
