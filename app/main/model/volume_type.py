
from .. import db, flask_bcrypt
from ..util import commonModelAttributes

class Volume_Type(db.Model,commonModelAttributes.CommonModelAttributes):
    """ Storevolume_type related details """
    __tablename__ = "volume_types"

    name = db.Column(db.String(128))


    def __repr__(self):
        return "<Volume_Type '{}'>".format(self.id)


