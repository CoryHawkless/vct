
from .. import db, flask_bcrypt
from ..util import commonModelAttributes


class Project(db.Model,commonModelAttributes.CommonModelAttributes):
    """ Project Model for storing project related details """
    __tablename__ = "project"

    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=True)


    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password_hash, password)


    def __repr__(self):
        return "<Project '{}'>".format(self.id)
