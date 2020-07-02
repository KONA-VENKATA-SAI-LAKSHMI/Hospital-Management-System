import os
from flask_sqlalchemy import SQLAlchemy
from hms import app, Flask

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "hospitalMS"

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HMS.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)