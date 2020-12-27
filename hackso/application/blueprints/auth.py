# -*- coding: utf-8 -*-
"""
    :author: Harumonia
    :url: http://harumonia.top
    :copyright: © 2020 harumonia<zxjlm233@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
import os
import time
from hashlib import md5

from flask import render_template, redirect, url_for, Blueprint, request, jsonify, flash
from werkzeug.utils import secure_filename
from application.extensions import db
from application.models import Comment, File
from application.models.user import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/get_basic_info', methods=['POST'])
def get_basic_info():
    data = request.json
    file = File.query.filter_by(file_name=data['file_name']).first()
    comments = file.comments
    return jsonify({'file': file.to_json(), 'comments': [foo.to_json() for foo in comments[:10]]})


@auth_bp.route('/get_comment', methods=['POST'])
def get_comment():
    data = request.json
    file = File.query.filter_by(file_name=data['file_name']).first()
    comments = file.comments
    return jsonify({'comments': [foo.to_json() for foo in comments[:10]]})


@auth_bp.route('/set_comment', methods=['POST'])
def set_comment():
    data = request.json
    signature = md5(str(data['userinfo']).encode()).hexdigest()
    query_user = User.query.filter_by(signature=signature).first()
    file = File.query.filter_by(file_name=data['file_name']).first()
    if not file:
        return jsonify({'code': 400, 'msg': 'invalid file'})
    if query_user:
        userinfo = query_user
        comment = Comment(body=data['body'], author=userinfo, file=file, date=time.strftime('%Y-%m-%d %H:%M:%S'))
        db.session.add(comment)
        db.session.commit()

    else:
        userinfo = User(username=data['userinfo']['nickName'], sex=data['userinfo']['gender'],
                        country=data['userinfo']['country'], region=data['userinfo']['province'],
                        city=data['userinfo']['city'], signature=signature)
        db.session.add(userinfo)
        comment = Comment(body=data['body'], author=userinfo, file=file, date=time.strftime('%Y-%m-%d %H:%M:%S'))
        db.session.add(comment)
        db.session.commit()
    return jsonify({'code': 200, 'msg': 'success'})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['doc', 'm4a', 'jpg', 'jpeg', 'png', 'docx', 'mp3', 'mp4']
    # return True


@auth_bp.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.path.abspath('.') + '/application/static/files/', filename))

            author = User.query.filter_by(id=1).first()
            filee = File(location='static/files/' + filename,
                         file_name=filename, file_type=filename.rsplit('.', 1)[1].lower(), author=author)

            db.session.add(filee)
            db.session.commit()
            return jsonify({'msg': 'success', 'code': '200'})
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input name=filename>
      <input type=submit value=Upload>
    </form>
    '''


@auth_bp.route('/register')
def register():
    ...
    # iyates other
    # generate a random account for demo use
    # username = fake.user_name()
    # # make sure the generated username was not in database
    # while User.query.filter_by(username=username).first() is not None:
    #     username = fake.user_name()
    # password = fake.word()
    # user = User(username=username)
    # user.set_password(password)
    # db.session.add(user)
    # db.session.commit()
    #
    # todo = Todos(body=_('看书半小时'), done=False, author=user)
    # todo2 = Todos(body=_('完成一道算法题'), done=False, author=user)
    # todo3 = Todos(body=_('正念|反思'), done=False, author=user)
    # todo4 = Todos(body=_('吃水果'), done=True, author=user)
    # bill = Bills(payfor="吃饭", money=15, author=user)
    # bill2 = Bills(payfor="交通", money=4.5, author=user)
    # db.session.add_all([todo, todo2, todo3, todo4, bill, bill2])
    # db.session.commit()
    #
    # return jsonify(username=username, password=password, message=_('Generate success.'))


@auth_bp.route('/init_db')
def init_db():
    db.create_all()
    return jsonify({'msg': 'success'})
