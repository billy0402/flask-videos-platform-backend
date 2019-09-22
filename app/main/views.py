from flask import render_template, request
from sqlalchemy.exc import SQLAlchemyError

from . import main
from ..models import *
from ..response_handler import ResponseHandler


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/api/user/', methods=['GET', 'POST'], defaults={'user_id': None})
@main.route('/api/user/<int:user_id>/', methods=['GET', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return ResponseHandler.error(1)
            return ResponseHandler.read(user.serialize)
        else:
            users = User.query.all()
        return ResponseHandler.read([user.serialize for user in users])

    if request.method == 'POST':
        data = request.get_json()
        if data:
            try:
                user = User.query.get(data['user_id'])
                if user:
                    user.name = data['user_name']
                    user.photo = data['user_photo']
                    user.email = data['email']
                    user.update_at = db.func.now()
                    db.session.add(user)
                    db.session.commit()

                    return ResponseHandler.update()
                else:
                    user = User(
                        id=data['user_id'],
                        name=data['user_name'],
                        photo=data['user_photo'],
                        email=data['email']
                    )
                    db.session.add(user)
                    db.session.commit()

                    return ResponseHandler.create()
            except SQLAlchemyError:
                db.session.rollback()
                return ResponseHandler.error(2)
        return ResponseHandler.error(1)

    if request.method == 'DELETE':
        user = User.query.get(user_id)
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
            except SQLAlchemyError:
                db.session.rollback()
                return ResponseHandler.error(2)
            else:
                return ResponseHandler.delete()
        return ResponseHandler.error(1)


@main.route('/user_action', methods=['GET', 'POST'])
def user_action():
    return render_template('index.html')


@main.route('/recommend_videos', methods=['GET', 'POST'])
def recommend_videos():
    return render_template('index.html')


@main.route('/personal_videos', methods=['GET', 'POST'])
def personal_videos():
    return render_template('index.html')
