
from .. import db, flask_bcrypt
from ..util import commonModelAttributes

class Volume(db.Model,commonModelAttributes.CommonModelAttributes):
    """ Volume Model for storing volume related details """
    __tablename__ = "volumes"

    name =                      db.Column(db.String(128))
    description =               db.Column(db.String(256))
    type =                      db.Column(db.String(64),nullable=False)
    size =                      db.Column(db.Integer,nullable=False,default=0)


    def __repr__(self):
        return "<Volume '{}'>".format(self.id)
