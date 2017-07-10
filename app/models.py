from sqlalchemy import UniqueConstraint
import locale
import platform
from app import db, app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import flask_whooshalchemy

# The model for an User, User has id (Primariy key), username, password and email.
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(64), index=True, default='')
    password_hash = db.Column(db.String(160), default='')
    email = db.Column(db.String(120), index=True, unique=True, default='')

    def __init__(self, display_name='', password='', email=''):
        self.display_name = display_name
        self.password_hash = generate_password_hash(password)
        self.email = email

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Tries to log a user in with a password and an email, returns false if no user & pass does not exist or match
    @classmethod
    def authenticate(cls, email, password):
        user = User.query.filter(db.or_(User.email == email)).first()
        if user.check_password(password):
            cls.is_authenticated = True
            return user
        else:
            return False

    @classmethod
    def get(cls, id):
        return User.query.filter(db.or_(User.id == id)).first()
    #TODO a correct is_authenticated, see authenticate for why it returns true now.
    # Returns true if user is logged in
    @property
    def is_authenticated(self):
        return False

    # Returns true if the user is logged in.
    @property
    def is_active(self):
        return True

    # Returns false, user is not anonymous.
    @property
    def is_anonymous(self):
        return False

    @property
    def set_user(self):
        self.id = self

    # Represents the user with its id
    def get_id(self):
            return str(self.id)  # python 3

    # Returns the username of the user
    def __repr__(self):
        return '<User %r>' % self.display_name

