
from .. import db, flask_bcrypt
from ..util import commonModelAttributes

class Volume_Type(db.Model,commonModelAttributes.CommonModelAttributes):
    """ Volume_Type Model for storing volume_type related details """
    __tablename__ = "volume_types"

    name =                      db.Column(db.String(128))
    description =               db.Column(db.String(256))

    def __repr__(self):
        return "<Volume_Type '{}'>".format(self.id)
