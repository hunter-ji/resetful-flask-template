# -*- coding: utf-8 -*-
from server import app
import os

# 获取环境变量FLASK_MODULE来切换开发与生产环境
# flask_module为production时为生产环境，其余皆为开发环境
flask_module = os.getenv('FLASK_MODULE')

SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))

RESTFUL_JSON = dict(ensure_ascii = False)

# sqlite3
dev_db = 'sqlite:////' + os.path.join(os.path.dirname(app.root_path), 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_POOL_RECYCLE = 280
