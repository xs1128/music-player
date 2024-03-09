from flask import Flask, url_for, request, render_template, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    # Name of file executed
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsad#shdahij!!#(SIODA*)'
    # configure the SQLite database, relative to the app instance folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initialize the app with the extension
    db.init_app(app)

    from .views import views
    from .auth import auth
    # Register blueprint and modify prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # If import .xxx, need import .xxx as xxx
    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


