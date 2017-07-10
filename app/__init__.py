from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib import sqla
from flask_basicauth import BasicAuth
from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Response
from config import ADMIN_USERNAME, ADMIN_PASSWORD, WHOOSH_BASE
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
mail = Mail(app)

from app import views, models, db

app.config['BASIC_AUTH_USERNAME'] = ADMIN_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = ADMIN_PASSWORD

app.config['WHOOSH_BASE'] = WHOOSH_BASE


class AuthException(HTTPException):
    def __init__(self, message):
        super(AuthException, self).__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

basic_auth = BasicAuth(app)


class ModelView(sqla.ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())




admin = Admin(app, name="Admin Page", template_mode="bootstrap3")
admin.add_view(ModelView(models.User, db.session))