from app import app
from os import environ

port = int(environ.get('PORT', 5000))
app.run(host= '0.0.0.0', debug=True, port=port, threaded = True)