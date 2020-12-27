"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: user.py
@time: 2020/8/15 20:17
@desc:
"""
from application.extensions import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')
    username = db.Column(db.String(20), comment='用户名')
    signature = db.Column(db.String(40), comment='用户签名')
    region = db.Column(db.String(20), comment='省份')
    city = db.Column(db.String(20), comment='城市')
    country = db.Column(db.String(20), comment='国家')
    sex = db.Column(db.Integer, comment='性别')
    # last_login = db.Column(db.DateTime, comment='最后登录日期')
    # last_ip = db.Column(db.String(16), comment='最后登录日期')
