from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String
from flask_login import UserMixin

db = SQLAlchemy(app)


class User(UserMixin):
    email = Column(String(80), primary_key=True, unique=True)
    password = Column(String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

