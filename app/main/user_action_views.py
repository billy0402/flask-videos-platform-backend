from flask import request
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from .. import db
from ..models.action_models import ActionType, UserAction
from ..models.user_models import User
from ..models.video_models import Video
from ..response_handler import ResponseHandler


class UserActionView(Resource):
    def get(self, user_action_id):
        user_action = UserAction.query.get(user_action_id)
        if not user_action:
            return ResponseHandler.error(1)
        return ResponseHandler.read(user_action)


class UserActionList(Resource):
    def get(self):
        user_actions = UserAction.query.all()
        return ResponseHandler.list(user_actions)

    def post(self):
        data = request.get_json()
        if not data:
            return ResponseHandler.error(3)

        try:
            user = User.query.get(data['user_id'])
            action_type = ActionType.query.get(data['action_type'])
            video_id = data['current_video']['video_id']
            video_type = data['current_video']['video_type']
            video = Video.query.filter_by(id=video_id, video_type_id=video_type).first()

            user_action = UserAction(
                user=user,
                action_type=action_type,
                video=video,
                video_time=data['video_time']
            )
            db.session.add(user_action)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ResponseHandler.error(2)
        return ResponseHandler.create()
