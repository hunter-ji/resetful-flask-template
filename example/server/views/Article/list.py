from server import api
from flask_restful import Resource
from server.models import Article
from flask import g


class ArticleList(Resource):

    def get(self):
        articles = Article.query.filter_by(
            author_id = g.uid
        ).order_by(Article.add_time.desc()).all()
        return {
            'code': 20000,
            'data': [
                {
                    'title':   article.title,
                    'content': article.content
                }
                for article in articles
            ]
        }


api.add_resource(ArticleList, '/article/list')
