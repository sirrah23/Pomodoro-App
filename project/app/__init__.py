import os
from flask import Flask, render_template
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from project.app.config import BaseConfig
from project.app.logger import getHandler

basedir = os.path.abspath(os.path.dirname(__file__))

# Set up the app
app = Flask(__name__)
app.config.from_object(BaseConfig)
app.logger.addHandler(getHandler())
db = SQLAlchemy(app)

# Set up the login manager
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.init_app(app)

app.logger.info('Application has been initialized')

from . import views
