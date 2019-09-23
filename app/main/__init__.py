import re

from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

from .personal_video_views import PersonalVideoView, PersonalVideoList
from .recommend_video_views import RecommendVideoView, RecommendVideoList
from .user_action_views import UserActionView, UserActionList
from .user_views import UserView, UserList

main = Blueprint('main', __name__)
CORS(main, resources={r'/api/*': {'origins': re.compile(
    r'^https?://(?:localhost:(?:3000|5000)|140\.131\.115\.53|videos-platform-backend\.herokuapp\.com)$'
)}})

api = Api(main)
api.add_resource(UserList, '/api/user/')
api.add_resource(UserView, '/api/user/<int:user_id>/')
api.add_resource(UserActionList, '/api/user_action/')
api.add_resource(UserActionView, '/api/user_action/<int:user_action_id>/')
api.add_resource(RecommendVideoList, '/api/recommend_video/')
api.add_resource(RecommendVideoView, '/api/recommend_video/<int:video_id>/')
api.add_resource(PersonalVideoList, '/api/personal_video/')
api.add_resource(PersonalVideoView, '/api/personal_video/<int:video_id>/')

from . import views, errors
