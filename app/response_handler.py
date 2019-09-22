class ResponseHandler:
    @staticmethod
    def create():
        return {'result': True}, 201

    @staticmethod
    def read(data):
        return {'result': True, 'data': data.serialize}, 200

    @staticmethod
    def list(datas):
        return {'result': True, 'data': [data.serialize for data in datas]}, 200

    @staticmethod
    def update():
        return {'result': True}, 200

    @staticmethod
    def delete():
        return {'result': True}, 204

    @staticmethod
    def error(error_code):
        error_msg_dict = {
            1: {'message': 'Data not Found', 'status_code': 404},
            2: {'message': 'SQL error', 'status_code': 400},
            3: {'message': 'No request data', 'status_code': 404},
        }
        error_msg = error_msg_dict[error_code]['message']
        status_code = error_msg_dict[error_code]['status_code']
        return {'result': False, 'errorCode': error_code, 'errorMessage': error_msg}, status_code
