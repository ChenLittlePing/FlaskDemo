from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Database
# 配置 sqlalchemy  "数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码"
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:root@localhost:5000/dbjangoDB?charset=utf8"

engine = create_engine(SQLALCHEMY_DATABASE_URI,  echo=True)

Session = sessionmaker(bind=engine)

