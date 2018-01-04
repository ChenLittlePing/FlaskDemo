from flask import jsonify
from .bp import bp
from models import User
from db import db
import json


@bp.route('/', methods=['GET', 'POST'])
def index():
    js = {
        'message': 1,
        'error': 0,
        'data': [{'pos': 1}, {'pos': 2}]
    }
    return jsonify(js)


@bp.route('/<string:name>/<int:pwd>')
def login(name, pwd):
    user = User(name, pwd)
    db.session.add(user)
    db.session.commit()
    return "创建用户 %s, 密码 %d" % (name, pwd)


@bp.route('/login/<string:name>')
def loginByName(name):
    user = User.query.filter(User.name == name).first()
    if user is None or user.name.strip == '':
        return '用户不存在'
    else:
        return '%s 用户登陆' % user.name


@bp.route('/checkout')
def checkAll():
    user = User.query.all()
    print(user)
    return json.dumps({'data': [{'name': u.name, 'pwd': u.thrust} for u in user]}, indent=4)


@bp.route('/update/<string:name>/<string:pwd>')
def update(name, pwd):
    user = User.query.filter(User.name == name).first()
    if user is not None:
        user.thrust = pwd
        db.session.commit()
        return '修改 用户 %s ,密码为：%s' % (name, pwd)
    else:
        return '用户不存在'


@bp.route('/delete/<string:name>/<string:pwd>')
def delete(name, pwd):
    user = User.query.filter(User.name == name, User.thrust == pwd).first()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return '删除 用户 %s ,密码为：%s' % (name, pwd)
    else:
        return '用户不存在，或密码不正确'
