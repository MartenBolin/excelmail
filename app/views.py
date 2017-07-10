from flask import render_template, request, flash, redirect, url_for, jsonify, g, abort
from app import app, db, lm
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')