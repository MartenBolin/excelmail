from app import app
from os import environ

app.run(host= '0.0.0.0', debug=True, port=environ.get("PORT", 5000), threaded = True)