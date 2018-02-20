from login_app.app import db

from sqlalchemy import Column, String
from flask_login import UserMixin
from .config import SQLALCHEMY_DATABASE_URI


class User(UserMixin):
    email = db.Column(String(80), primary_key=True, unique=True)
    password = db.Column(String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

