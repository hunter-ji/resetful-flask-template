from server import api, db
from server.models import User
from flask_restful import Resource, reqparse
from flask import g
from server.utils.encrytion import convert_to_md5


class ChangePass(Resource):

    # 更换密码
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('old_pass', type = str, required = True)
        parse.add_argument('new_pass', type = str, required = True)
        args = parse.parse_args()

        old_pass = convert_to_md5(args.old_pass)
        new_pass = convert_to_md5(args.new_pass)

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
