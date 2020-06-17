# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restful import Api
from flask_migrate import Migrate
from server.utils.redisConn import RedisConn

app = Flask('server')
app.config.from_pyfile('config.py')

CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
redis = RedisConn()

from server import commands
from server.interceptor import intercept
from server.views.User import authenticate, info
from server.views.Article import list
