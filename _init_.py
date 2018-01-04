from flask import Flask
from admin.bp import bp as admin_bp
from db import db


app = Flask(__name__)

app.config.from_object('config')

app.register_blueprint(admin_bp)

with app.app_context():
    db.init_app(app)
    db.create_all()

