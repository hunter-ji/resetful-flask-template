from server import api, redis
from flask_restful import Resource, reqparse
from flask import g
from server.models import User
from server.utils.encrytion import convert_to_md5

import time


class Login(Resource):

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('username', type = str, required = True)
        parse.add_argument('password', type = str, required = True)
        args = parse.parse_args()

        # 查询是否为已注册用户
        user_info_check = User.query.filter_by(
            username = args.username
        ).first()
        if not user_info_check:
            return {
                'code':    20001,
                'message': '不存在该用户'
            }

        if user_info_check.password != args.password:
            return {
                'code':    20001,
                'message': '密码错误'
            }

        # 加密信息获取token
        token = convert_to_md5('{0}true{1}false{2}'.format(
            args.username,
            args.password,
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
