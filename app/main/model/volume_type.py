
from .. import db, flask_bcrypt

class Volume(db.Model):
    """ Volume Model for storing volume related details """
    __tablename__ = "volumes"

    id =                        db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at =                db.Column(db.DateTime, nullable=False)
    deleted =                   db.Column(db.Boolean, nullable=False, default=False)
    name =                      db.Column(db.String(128))
    description =               db.Column(db.String(256))
    type =                      db.Column(db.String(64),nullable=False)
    size =                      db.Column(db.Integer,nullable=False,default=0)


    def __repr__(self):
        return "<Volume '{}'>".format(self.volumename)
