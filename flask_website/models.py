from datetime import datetime
from flask_website import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    table = db.Column(db.Integer)
    bonus = db.Column(db.Integer)
    status = db.relationship('Order', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)




@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('user.id'))
    status = db.Column(db.String(64), default=False)


    def __repr__(self):
        return '<Status {}>'.format(self.status)

