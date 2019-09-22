from flask import jsonify


class ResponseHandler:
    @staticmethod
    def create():
        return jsonify({'result': True}), 201

    @staticmethod
    def read(data):
        return jsonify({'result': True, 'data': data}), 200

    @staticmethod
    def update():
        return jsonify({'result': True}), 200

    @staticmethod
    def delete():
        return jsonify({'result': True}), 204

    @staticmethod
    def error(error_code):
        error_msg_dict = {
            1: {'message': 'No data', 'status_code': 404},
            2: {'message': 'SQL error', 'status_code': 400},
        }
        error_msg = error_msg_dict[error_code]['message']
        status_code = error_msg_dict[error_code]['message']
        return jsonify({'result': False, 'errorCode': error_code, 'errorMessage': error_msg}), status_code
