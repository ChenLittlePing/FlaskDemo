from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from db import engine

Base = declarative_base()


# 用户表
class User(Base):

    # Columns

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(64), unique=True, index=True)

    thrust = Column(Integer, default=0)

    def __init__(self, name, thrust):
        self.name = name
        self.thrust = thrust

    def __repr__(self):
        return '<User %r>' % self.name

    def __str__(self):
        return '<User %s>' % self.name


class Comment(Base):

    # Columns

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(64), unique=True, index=True)

    desc = Column(String(128))

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return '<User %r>' % self.desc

    def __str__(self):
        return '<User %s>' % self.desc

Base.metadata.create_all(engine)

