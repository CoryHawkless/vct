
from .. import db, flask_bcrypt

class Volume_Type(db.Model):
    """ Volume_Type Model for storing volume_type related details """
    __tablename__ = "volume_types"

    id =                        db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at =                db.Column(db.DateTime, nullable=False)
    deleted =                   db.Column(db.Boolean, nullable=False, default=False)
    name =                      db.Column(db.String(128))
    description =               db.Column(db.String(256))

    def __repr__(self):
        return "<Volume_Type '{}'>".format(self.id)
