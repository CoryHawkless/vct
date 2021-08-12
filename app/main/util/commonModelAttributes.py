
from .. import db
import datetime


class CommonModelAttributes(object):
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    deleted_at = db.Column(db.DateTime, default=datetime.datetime.now())
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)