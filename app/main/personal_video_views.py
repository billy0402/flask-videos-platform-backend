from flask_restful import Resource

from ..models.video_models import Video
from ..response_handler import ResponseHandler


class PersonalVideoView(Resource):
    def get(self, video_id):
        video = Video.query.get(video_id)
        if not video:
            return ResponseHandler.error(1)
        return ResponseHandler.read(video)


class PersonalVideoList(Resource):
    def get(self):
        videos = Video.query.order_by(db.func.random()).limit(10)
        return ResponseHandler.list(videos)
