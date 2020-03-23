# -*- coding: utf-8 -*-
import os

# 获取环境变量FLASK_MODULE来切换开发与生产环境
# flask_module为production时为生产环境，其余皆为开发环境
flask_module = os.getenv('FLASK_MODULE')

SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))

RESTFUL_JSON = dict(ensure_ascii = False)

# sqlite3
# dev_db = 'sqlite:////' + os.path.join(os.path.dirname(app.root_path), 'data.db')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)


# mariadb/mysql
if flask_module == 'production':
    # 生产环境
    # mariadb/mysql
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABSE = 'example'
    USERNAME = 'kuari'
    PASSWORD = 'password'

    # redis
    REDIS_HOSTNAME = '127.0.0.1'
    REDIS_PORT = 6379
else:
    # 开发环境
    # mariadb/mysql
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABSE = 'example'
    USERNAME = 'kuari'
    PASSWORD = 'password'

    # redis
    REDIS_HOSTNAME = '127.0.0.1'
    REDIS_PORT = 6379

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABSE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_POOL_RECYCLE = 280
