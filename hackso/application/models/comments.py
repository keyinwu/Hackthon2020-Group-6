"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: comments.py
@time: 2020/12/26 13:46
@desc:
"""

from application.extensions import db


class Comment(db.Model):
    __tablename__ = 'tb_comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='id')
    body = db.Column(db.Text, nullable=False, comment='内容')
    date = db.Column(db.Date)
    author_id = db.Column(db.ForeignKey('tb_user.id', ondelete='CASCADE', onupdate='CASCADE'), comment='关联对象')
    author = db.relationship('User', primaryjoin='Comment.author_id == User.id', backref='comments')
    file_id = db.Column(db.ForeignKey('tb_file.id', ondelete='CASCADE', onupdate='CASCADE'), comment='关联对象')
    file = db.relationship('File', primaryjoin='Comment.file_id == File.id', backref='comments')

    def to_json(self):
        return {
            'body': self.body,
            'author': self.author.username,
            'date': self.date
        }
