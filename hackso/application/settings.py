# -*- coding: utf-8 -*-
"""
    :author: Harumonia
    :url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os

# basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    TODOISM_LOCALES = ['en_US', 'zh_Hans_CN']
    TODOISM_ITEM_PER_PAGE = 20

    SSL_CONTEXT = 'adhoc'

    BABEL_DEFAULT_LOCALE = TODOISM_LOCALES[0]

    # SERVER_NAME = 'application.dev:5000'  # enable subdomain support
    SECRET_KEY = os.getenv('SECRET_KEY', 'a secret string')

    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@39.108.229.166/hackson'
    # flask-sqlacodegen "mysql://root:root@39.108.229.166/yoyodaily" --outfile "application/slide.py" --flask

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost/hackson'


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
