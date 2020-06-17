# -*- coding: utf-8 -*-
import click

from server import app, db
from server.models import User, Article
from faker import Faker
from server.utils.encrytion import convert_to_md5


@app.cli.command()
@click.option('--drop', is_flag = True, help = 'Create after drop.')
def initdb(drop):
    """初始化数据库"""
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort = True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
def initdata():
    fake = Faker('zh_CN')
    #  插入用户信息
    for _ in range(10):
        new_user = User(
            username = fake.name(),
            password = convert_to_md5('adminadmin')
        )
        db.session.add(new_user)

    for i in range(10):
        new_article = Article(
            title = 'title{}'.format(i),
            content = 'content{}'.format(i),
            author_id = 1
        )
        db.session.add(new_article)
    db.session.commit()
