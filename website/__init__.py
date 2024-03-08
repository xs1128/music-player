from flask import Flask, url_for, request, render_template, redirect, abort
from flask_sqlalchemy import SQLAlchemy

def create_app():
    # Name of file executed
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsad#shdahij!!#(SIODA*)'

    from .views import views
    from .auth import auth

    # Register blueprint and modify prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app