import re

from flask import Blueprint
from flask_cors import CORS
from flask_restful import Api

from .user_views import UserView, UserList

main = Blueprint('main', __name__)
CORS(main, resources={r'/api/*': {'origins': re.compile(
    r'^https?://(?:localhost:(?:3000|5000)|140\.131\.115\.53|videos-platform-backend\.herokuapp\.com)$'
)}})

api = Api(main)
api.add_resource(UserList, '/api/user/')
api.add_resource(UserView, '/api/user/<int:user_id>/')

from . import views, errors
