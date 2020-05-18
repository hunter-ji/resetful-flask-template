from server import api, app
from flask_restful import Resource
from flask import send_from_directory, send_file
from datetime import datetime

import os


class Download(Resource):

    # url下载
    def get(self, filename):
        return send_from_directory(os.path.join(app.root_path, 'uploads'), filename)

    # 文件流下载
    def post(self):
        filename = g.username + str(datetime.now().strftime('%Y-%m-%d')) + '.xlsx'
        # 自行生成file_stream
        file_stream = '文件流'
        return send_file(
            file_stream,
            as_attachment = True,
            attachment_filename = filename
        )


api.add_resource(Download, '/file/uploads')
