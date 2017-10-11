from datetime import datetime

from app import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String)
    pomodoros = db.relationship('Pomodoro', backref='user', lazy='dynamic')

    @property
    def password(self, password):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    def __repr__(self):
        return "<User {}>".format(self.username)


class Pomodoro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    length_seconds = db.Column(db.Integer, default=1500)  # Default 25 minutes
    end_time = db.Column(db.DateTime, default=datetime.utcnow)
    context = db.Column(db.String(80), default="")
    interruptions = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @staticmethod
    def create_new_pomodoro(context, interruptions, user_id):
        pomodoro = Pomodoro(context=context,
                            interruptions=interruptions,
                            user_id=user_id)
        db.session.add(pomodoro)
        db.session.commit()

    @staticmethod
    def pomodoros_past_n_days(n, user):
        pass
