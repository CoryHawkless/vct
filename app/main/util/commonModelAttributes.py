from .. import db
import datetime
from sqlalchemy.ext.declarative import declared_attr



class CommonModelAttributes(object):
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, nullable=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        db.session.add(self)
        db.session.flush()
        return self