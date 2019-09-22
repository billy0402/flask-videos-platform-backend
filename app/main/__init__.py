import re

from flask import Blueprint
from flask_cors import CORS

main = Blueprint('main', __name__)
CORS(main, resources={r'/api/*': {'origins': re.compile(
    r'^https?://(?:localhost:(?:3000|5000)|videos-platform-backend.herokuapp.com)$'
)}})

from . import views, errors
