from server import api, db
from server.models import User
from flask_restful import Resource
from flask import request, g


class UserInfo(Resource):

    # 用户信息
    def get(self):
        user_info = User.query.filter_by(uid = g.uid).first()
        return {
            'uid':      user_info.uid,
            'username': user_info.username
        }

    # 信息修改
    def post(self):
        data = request.get_json()
        username = data.get('username')

        user_info = User.query.filter_by(uid = g.uid).first()
        user_info.username = username

        db.session.commit()
        return {
            'code': 20000
        }


api.add_resource(UserInfo, '/user/info')
