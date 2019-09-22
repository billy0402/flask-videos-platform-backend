from flask import request
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

from ..models import *
from ..response_handler import ResponseHandler


class UserView(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return ResponseHandler.error(1)
        return ResponseHandler.read(user)

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return ResponseHandler.error(1)

        try:
            db.session.delete(user)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ResponseHandler.error(2)
        return ResponseHandler.delete()

    def put(self, user_id):
        data = request.get_json()
        user = User.query.get(user_id)
        if not data:
            return ResponseHandler.error(3)
        elif not user:
            return ResponseHandler.error(1)

        try:
            user.name = data.get('user_name', user.name)
            user.photo = data.get('user_photo', user.photo)
            user.email = data.get('email', user.email)
            user.update_at = db.func.now()
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            return ResponseHandler.error(2)
        return ResponseHandler.update()


class UserList(Resource):
    def get(self):
        users = User.query.all()
        return ResponseHandler.list(users)

    def post(self):
        data = request.get_json()
        user = User.query.get(data['user_id'])
        if not data:
            return ResponseHandler.error(3)

        try:
            if user:
                user.name = data.get('user_name', user.name)
                user.photo = data.get('user_photo', user.photo)
                user.email = data.get('email', user.email)
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
