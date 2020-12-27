"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: files.py
@time: 2020/12/26 16:26
@desc:
"""
from application.extensions import db


class File(db.Model):
    __tablename__ = 'tb_file'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')
    location = db.Column(db.Text, nullable=False, comment='文件位置')
    file_type = db.Column(db.String(20), nullable=False, comment='文件类型')
    file_name = db.Column(db.String(20), nullable=False, comment='文件名')
    date = db.Column(db.Date)
    author_id = db.Column(db.ForeignKey('tb_user.id', ondelete='CASCADE', onupdate='CASCADE'), comment='关联对象')
    author = db.relationship('User', primaryjoin='File.author_id == User.id', backref='files')

    def to_json(self):
        return {
            'filename': self.file_name,
            'author': self.author.username
        }
