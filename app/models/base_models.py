from .. import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
    update_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
