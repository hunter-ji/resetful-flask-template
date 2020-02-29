# -*- coding: utf-8 -*-
from server import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    avatar_id = db.Column(db.Integer, nullable = False, default = 0)
    username = db.Column(db.String(10), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    reg_time = db.Column(db.DateTime, default = datetime.now())
    last_login_time = db.Column(db.DateTime, default = datetime.now())


class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(20), nullable = False)
    content = db.Column(db.Text, nullable = False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship('User', backref = db.backref('articles'))
