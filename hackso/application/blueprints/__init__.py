"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: __init__.py.py
@time: 2020/12/26 13:47
@desc:
"""
from application.blueprints.auth import auth_bp
from application.blueprints.stream import stream_bp

all_bp = [
    auth_bp,
    stream_bp
]