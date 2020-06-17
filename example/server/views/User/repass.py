from server import api, db
from server.models import User
from flask_restful import Resource
from flask import request, g
from server.utils.encrytion import convert_to_md5


class ChangePass(Resource):

    # 更换密码
    def post(self):
        data = request.get_json(force = True)
        old_pass = convert_to_md5(data.get('old_pass'))
        new_pass = convert_to_md5(data.get('new_pass'))

        user_info = User.query.fileter_by(uid = g.uid).first()
        if old_pass != user_info.password:
            return {
                'code':    50008,
                'message': '原密码不对'
            }

        user_info.password = new_pass
        db.session.commit()

        return {
            'code': 20000
        }


api.add_resource(ChangePass, '/user/repass')
