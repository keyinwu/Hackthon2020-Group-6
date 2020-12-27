# -*- coding: utf-8 -*-
"""
    :author: Harumonia
    :url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
