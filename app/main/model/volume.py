
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from typing import Union


class Volume(db.Model):
    """ Volume Model for storing volume related details """
    __tablename__ = "volumes"

    id =                        db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at =                db.Column(db.DateTime, nullable=False)
    deleted =                   db.Column(db.Boolean, nullable=False, default=False)
    name =                      db.Column(db.String(128))
    description =               db.Column(db.String(256))


    def __repr__(self):
        return "<Volume '{}'>".format(self.volumename)
