from flask_app import db
import uuid
from sqlalchemy import Column, String, Integer
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(Integer(), primary_key=True)
    email = db.Column(String(80), unique=True)
    password = db.Column(String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email

