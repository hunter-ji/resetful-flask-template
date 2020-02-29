from werkzeug.utils import secure_filename
from server import app, api
from flask_restful import Resource
from flask import request
import time

import os


class Uploads(Resource):

    def option(self):
        return {
            'code': 20000
        }

    def post(self):
        file = request.files['file']
        file_type = secure_filename(file.filename).split('.')[-1]
        filename = str(time.time()).replace('.', '') + '.' + file_type
        file.save(os.path.join(app.root_path, 'uploads', filename))
        return {
            'code':     20000,
            'filename': filename
        }


api.add_resource(Uploads, '/file/uploads')
