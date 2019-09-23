from .base_models import BaseModel
from .. import db


class VideoType(BaseModel):
    __tablename__ = 'video_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    videos = db.relationship('Video', backref='video_type', lazy='dynamic')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name
        }

    def __repr__(self):
        return f'<VideoType {self.name!r}>'


class Video(BaseModel):
    __tablename__ = 'video'
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64))
    fan_page_id = db.Column(db.String(64), nullable=True)
    video_type_id = db.Column(db.Integer, db.ForeignKey('video_type.id'))
    user_actions = db.relationship('UserAction', backref='video', lazy='dynamic')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'video_name': self.name,
            'fan_page_id': self.fan_page_id,
            'video_type': self.video_type.name
        }

    def __repr__(self):
        return f'<VideoType {self.name!r}>'
