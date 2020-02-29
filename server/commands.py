# -*- coding: utf-8 -*-
import click

from server import app, db
from server.models import User
from faker import Faker
from random import randint


@app.cli.command()
@click.option('--drop', is_flag = True, help = 'Create after drop.')
def initdb(drop):
    """Initialize the database."""
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
            password = str(randint(10000, 99999))
        )
        db.session.add(new_user)
    db.session.commit()
