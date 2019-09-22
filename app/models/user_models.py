from .base_models import BaseModel
from .. import db


class User(BaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    photo = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            "user_id": self.id,
            "user_name": self.name,
            "user_photo": self.photo,
            "email": self.email
        }

    def __repr__(self):
        return f'<User {self.name!r}>'
