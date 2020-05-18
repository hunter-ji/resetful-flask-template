from server import api, redis
from flask_restful import Resource
from flask import request, g
from server.models import User
from server.utils.encrytion import convert_to_md5

import time


class Login(Resource):

    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = convert_to_md5(data.get('password'))

        # 查询是否为已注册用户
        user_info_check = User.query.filter_by(
            username = username,
            password = password
        ).first()
        if not user_info_check:
            return {
                'code':    40001,
                'message': '不存在该用户'
            }

        # 加密信息获取token
        token = convert_to_md5('{0}true{1}false{2}'.format(
            username,
            password,
            str(time.time())
        ))

        # 将信息写入redis
        redis.set(token,
                  {
                      'uid':      user_info_check.uid,
                      'username': user_info_check.username
                  })

        return {
            'code': 20000,
            'data': {
                'token': token
            }
        }


class Logout(Resource):

    def post(self):
        redis.delete(g.token)
        return {
            'code': 2000
        }


api.add_resource(Login, '/user/login')
api.add_resource(Logout, '/user/logout')
