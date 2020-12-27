"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: __init__.py.py
@time: 2020/12/26 13:46
@desc:
"""
import os

from flask import Flask
from application.blueprints import all_bp
from application.extensions import db, migrate
import application.models
from application.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('application')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    # register_commands(app)
    # register_errors(app)
    # register_template_context(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    for bp in all_bp:
        app.register_blueprint(bp)
