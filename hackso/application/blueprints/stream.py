"""
@author: harumonia
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: zxjlm233@gmail.com
@software: Pycharm
@file: stream.py
@time: 2020/12/26 13:57
@desc:
"""
from flask import Blueprint, Response, jsonify

stream_bp = Blueprint('stream', __name__)


@stream_bp.route('/')
def test_api():
    return jsonify({'hello': 'wx'})


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@stream_bp.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    # return Response(gen(Camera()),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')
