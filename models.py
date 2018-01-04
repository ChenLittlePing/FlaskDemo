from db import db


class User(db.Model):

    # Columns

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(64), unique=True, index=True)

    thrust = db.Column(db.Integer, default=0)

    def __init__(self, name, thrust):
        self.name = name
        self.thrust = thrust

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return '<User %s>' % self.name


class Comment(db.Model):

    # Columns

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(64), unique=True, index=True)

    desc = db.Column(db.String(128))

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return '<User %r>' % self.desc

    def __str__(self):
        return '<User %s>' % self.desc

