import os

base_dir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(base_dir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
WHOOSH_BASE = "whoosh"

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

stripe_keys = {
  'secret_key': ' sk_test_ZNm9sE9PTGXxlM77X5CKQju5',
  'publishable_key': 'pk_test_eCJ8lWbCknbXX0NGTECtP0sJ'
}

# This setups the mail server to be used for sending mails.
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'spacefinder1337@gmail.com'
MAIL_PASSWORD = 'password1337'

# administrator list
ADMINS = ['spacefinder1337@gmail.com']

#Sets number of ads per page
POSTS_PER_PAGE = 6