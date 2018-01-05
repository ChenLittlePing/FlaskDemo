from flask import jsonify
from .bp import bp
from models import User
from db import Session
import json
from flask import request


@bp.route('/', methods=['GET', 'POST'])
def index():
    js = {
        'message': 1,
        'error': 0,
        'data': [{'pos': 1}, {'pos': 2}]
    }
    return jsonify(js)


# 数据库 ： 增
@bp.route('/<string:name>/<int:pwd>')
def login(name, pwd):
    session = Session()
    user = User(name, pwd)
    session.add(user)
    session.commit()
    return "创建用户 %s, 密码 %d" % (name, pwd)


# 数据库 ： 查
@bp.route('/login/<string:name>')
def loginByName(name):
    session = Session()
    user = session.query(User).filter(User.name == name).first()
    session.close()
    if user is None or user.name.strip == '':
        return '用户不存在'
    else:
        return '%s 用户登陆' % user.name


# 数据库 ： 查
@bp.route('/checkout')
def checkAll():
    session = Session()
    user = session.query(User).all()
    session.close()
    print(user)
    return json.dumps({'data': [{'name': u.name, 'pwd': u.thrust} for u in user]}, indent=4)


# 数据库 ： 改
@bp.route('/update/<string:name>/<string:pwd>')
def update(name, pwd):
    user = User.query.filter(User.name == name).first()
    if user is not None:
        session = Session()
        user.thrust = pwd
        session.commit()
        session.close()
        return '修改 用户 %s ,密码为：%s' % (name, pwd)
    else:
        return '用户不存在'


# 数据库 ： 删
@bp.route('/delete/<string:name>/<string:pwd>')
def delete(name, pwd):
    user = User.query.filter(User.name == name, User.thrust == pwd).first()
    if user is not None:
        session = Session()
        session.delete(user)
        session.commit()
        session.close()
        return '删除 用户 %s ,密码为：%s' % (name, pwd)
    else:
        return '用户不存在，或密码不正确'


@bp.route('/user', methods=['POST', 'GET'])
def user():
    # if request.method == 'POST':
        name = request.args.get('name')
        if name is not None and name != '':
            session = Session()
            usr = session.query(User).filter(User.name == name).first()

            if usr is not None:
                return '用户名：%s，密码：%s' % (usr.name, usr.thrust)
            else:
                return '没有该用户'

        else:
            return '参数不完整'
    # else:
    #     return '不能使用GET方式获取'

