from flask_sqlalchemy import SQLAlchemy
import datetime
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    phone = db.Column(db.String(15))
    telegram_id = db.Column(db.String(25))

    def __init__(self, name, telegram_id):
        self.name = name
        self.telegram_id = telegram_id

    def __repr__(self):
        return '<User %r>' % self.name

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('users', lazy=True))

    def __init__(self, text, user, user_id):
        self.text = text
        self.user = user
        self.user_id = user_id

    def __repr__(self):
        return '<Message %r>' % self.text