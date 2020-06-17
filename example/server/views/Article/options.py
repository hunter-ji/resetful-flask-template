from server import api, db
from flask_restful import Resource, reqparse
from server.models import Article


class ArticleOptions(Resource):

    def get(self):
        """
        查看单个文章
        """
        parse = reqparse.RequestParser()
        parse.add_argument('article_id', type = int, required = True)
        args = parse.parse_args()

        article = Article.query.filter_by(
            article_id = args.article_id
        ).first()

        if not article:
            return {
                'code':    20001,
                'message': '该文章不存在'
            }

        return {
            'code': 20000,
            'data': {
                'title':     article.title,
                'content':   article.content,
                'author_id': article.author.username,
                'add_time':  article.add_time.strftime('%Y-%m-%d %H:%M:%S')
            }
        }

    def post(self):
        """
        新增文章
        """
        parse = reqparse.RequestParser()
        parse.add_argument('title', type = str, required = True)
        parse.add_argument('content', type = str, requird = True)
        parse.add_argument('author_id', type = int, required = True)
        args = parse.parse_args()

        article = Article(
            title = args.title,
            content = args.content,
            author_id = args.author_id
        )
        db.session.add(article)
        db.session.commit()

        return {
            'code': 20000
        }

    def put(self):
        """
        修改文章
        """
        parse = reqparse.RequestParser()
        parse.add_argument('article_id', type = str, required = True)
        parse.add_argument('title', type = str, required = False)
        parse.add_argument('content', type = str, required = False)
        parse.add_argument('author_id', type = int, requird = False)
        args = parse.parse_args()

        article = Article.query.filter_by(
            article_id = args.article_id
        ).first()

        if not article:
            return {
                'code':    20001,
                'message': '该文章不存在'
            }

        if args.title:
            article.title = args.title
        if args.content:
            article.content = args.content
        if args.author_id:
            article.author_id = args.author_id

        db.session.commit()

        return {
            'code': 20000
        }

    def delete(self):
        """
        删除文章
        """
        parse = reqparse.RequestParser()
        parse.add_argument('article_id', type = int, required = True)
        args = parse.parse_args()

        article = Article.query.filter_by(
            article_id = args.article_id
        ).first()

        if not article:
            return {
                'code':    20001,
                'message': '该文章不存在'
            }

        db.session.delete(article)
        db.session.commit()

        return {
            'code': 20000
        }


api.add_resource(ArticleOptions, '/article/options')
