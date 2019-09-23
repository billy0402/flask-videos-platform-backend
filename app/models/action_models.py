from .base_models import BaseModel
from .. import db


class ActionType(BaseModel):
    __tablename__ = 'action_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user_actions = db.relationship('UserAction', backref='action_type', lazy='dynamic')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name
        }

    def __repr__(self):
        return f'<ActionType {self.name!r}>'


class UserAction(BaseModel):
    __tablename__ = 'user_action'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    action_type_id = db.Column(db.Integer, db.ForeignKey('action_type.id'))
    video_id = db.Column(db.String(64), db.ForeignKey('video.id'))
    video_time = db.Column(db.Integer)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'user': self.user.serialize,
            'action_type': self.action_type.name,
            'action_time': self.create_at.strftime('%Y-%m-%d %H:%M:%S'),
            'current_video': self.video.serialize,
            'video_time': self.video_time
        }

    def __repr__(self):
        return f'<UserAction {self.action_type.name!r}>'
